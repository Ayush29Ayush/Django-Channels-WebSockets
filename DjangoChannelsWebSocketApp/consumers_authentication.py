# Topic - Django Channels with Authentication
import asyncio
import json
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from .models import Chat, Group
from channels.db import database_sync_to_async


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Websocket Connected...", event)
        print("Channel Layer...", self.channel_layer)
        print("Channel Name...", self.channel_name)  # get channel Name

        print("Dynamic Group Name...", self.scope["url_route"]["kwargs"]["group_ka_naam"])
        self.group_name = self.scope["url_route"]["kwargs"]["group_ka_naam"]
        print("Group Name...", self.group_name)
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

        self.send({"type": "websocket.accept"})

    def websocket_receive(self, event):
        print("Message Received from Client...", event["text"])
        print("Type of Message Received from Client...", type(event["text"]))
        data = json.loads(event["text"])
        print("Data...", data)
        print("Type of Data...", type(data))
        print("Chat Message", data["msg"])

        print("User => ", self.scope["user"])

        # Find Group Object
        group = Group.objects.get(name = self.group_name)
        if self.scope['user'].is_authenticated:
            # Create New Chat Object
            chat = Chat(
                content = data['msg'],
                group = group
            )
            chat.save()
            async_to_sync(self.channel_layer.group_send)(
                self.group_name, 
                {
                'type': 'chat.message',
                'message':event['text']
                }
            )
        else:
            self.send({
                'type':'websocket.send',
                'text': json.dumps({"msg":"Login Required"})
            })

    #! FLOW => The message sent by the client will be received by the websocket_receive() function, which will then be sent to the chat_message() function using the programmers group. Then the chat_message() function will do some processing and then send the response back to the client using the websocket.send consumer event.
    def chat_message(self, event):
        print("Event...", event)
        print("Actual Data...", event["message"])
        print("Type of Actual Data...", type(event["message"]))
        self.send({"type": "websocket.send", "text": event["message"]})

    def websocket_disconnect(self, event):
        print("Websocket Disconnected...", event)
        print("Channel Layer...", self.channel_layer)  # get default channel layer from a project
        print("Channel Name...", self.channel_name)  # get channel Name
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
  async def websocket_connect(self, event):
    print('Websocket Connected...', event)
    print("Channel Layer...", self.channel_layer)   # get default channel layer from a project
    print("Channel Name...", self.channel_name)   # get channel Name
    self.group_name = self.scope['url_route']['kwargs']['group_ka_naam']
    print("Group Name...", self.group_name)
    #  add a channel to a new or existing group
    await self.channel_layer.group_add(self.group_name,self.channel_name)
    await self.send({'type':'websocket.accept'})

  async def websocket_receive(self, event):
    print('Message Received from Client...', event['text'])
    print('Type of Message Received from Client...', type(event['text']))
    data = json.loads(event['text'])
    print("Data...", data)
    print("Type of Data...", type(data))
    print("Chat Message", data['msg'])
    # Find Group Object
    group = await database_sync_to_async(Group.objects.get)(name = self.group_name)
    if self.scope['user'].is_authenticated:
      # Create New Chat Object
      chat = Chat(
        content = data['msg'],
        group = group
      )
      await database_sync_to_async(chat.save)()
      data['user'] = self.scope['user'].username
      print("Complete Data...", data)
      print("Type of Complete Data...", type(data))
      await self.channel_layer.group_send(
        self.group_name, 
        {
          'type': 'chat.message',
          'message':json.dumps(data)
        }
      )
    else:
      await self.send({
        'type':'websocket.send',
        'text': json.dumps({"msg":"Login Required", "user":"guest"})
      })
  
  async def chat_message(self, event):
    print('Event...', event)
    print('Actual Data...', event['message'])
    print('Type of Actual Data...', type(event['message']))
    await self.send({
      'type': 'websocket.send',
      'text': event['message']
    })


  async def websocket_disconnect(self, event):
    print('Websocket Disconnected...', event)
    print("Channel Layer...", self.channel_layer)   # get default channel layer from a project
    print("Channel Name...", self.channel_name)   # get channel Name
    await self.channel_layer.group_discard(self.group_name, self.channel_name)
    raise StopConsumer()
  