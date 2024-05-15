# Topic - Chat App with Static Group Name
import asyncio
import json
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Websocket Connected...", event)
        print(
            "Channel Layer...", self.channel_layer
        )  # get default channel layer from a project
        print("Channel Name...", self.channel_name)  # get channel Name
        #! add a channel to a new or existing group
        # Here, programmers is the group name and we are adding self.channel_name into the group
        # self.channel_layer.group_add("programmers", self.channel_name)
        async_to_sync(self.channel_layer.group_add)("programmers", self.channel_name)

        self.send({"type": "websocket.accept"})

    def websocket_receive(self, event):
        print("Entire Event in websocket_receive:", event)
        print("Message Received from Client...", event["text"])
        print("Type of Message Received from Client...", type(event["text"]))
        async_to_sync(self.channel_layer.group_send)(
            "programmers", {"type": "chat.message", "message": event["text"]}
        )

    #! FLOW => The message sent by the client will be received by the websocket_receive() function, which will then be sent to the chat_message() function using the programmers group. Then the chat_message() function will do some processing and then send the response back to the client using the websocket.send consumer event.
    def chat_message(self, event):
        print("Event...", event)
        print("Actual Data...", event["message"])
        print("Type of Actual Data...", type(event["message"]))
        # Parse the JSON string to a dictionary
        message_data = json.loads(event["message"])
        print("Type of message_data...", type(message_data))
        # Extract the value of the "msg" key
        msg_value = message_data["msg"]
        # Concatenate "output_message" with the extracted value
        ayush_output_message = "output_message" + msg_value
        print("ayush_output_message =>", ayush_output_message)
        # self.send({"type": "websocket.send", "text": event["message"]})
        #! This will send the message to the client and will be received by ws.onmessage
        self.send({"type": "websocket.send", "text": ayush_output_message})

    def websocket_disconnect(self, event):
        print("Websocket Disconnected...", event)
        print(
            "Channel Layer...", self.channel_layer
        )  # get default channel layer from a project
        print("Channel Name...", self.channel_name)  # get channel Name
        async_to_sync(self.channel_layer.group_discard)(
            "programmers", self.channel_name
        )
        raise StopConsumer()


# class MyAsyncConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         print("Websocket Connected...", event)
#         await self.send(
#             {
#                 "type": "websocket.accept",
#             }
#         )

#     async def websocket_receive(self, event):
#         print("Message received from Client", event["text"])

#     async def websocket_disconnect(self, event):
#         print("Websocket Disconnected...", event)
#         raise StopConsumer()
