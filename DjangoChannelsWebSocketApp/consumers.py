# Topic - Consumer
from channels.consumer import SyncConsumer, AsyncConsumer


#! Here, MySyncConsumer inherits from the SyncConsumer class
class MySyncConsumer(SyncConsumer):
    # This handler is called when client initially opens a connection and is about to finish the WebSocket handshake.
    def websocket_connect(self, event):
        print("Websocket Connected...")

    # This handler is called when data received from Client
    def websocket_receive(self, event):
        print("Messaged Received...")

    # This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
    def websocket_disconnect(self, event):
        print("Websocket Disconnected...")


#! Here, MyAsyncConsumer inherits from the AsyncConsumer class
class MyAsyncConsumer(AsyncConsumer):
    # This handler is called when client initially opens a connection and is about to finish the WebSocket handshake.
    async def websocket_connect(self, event):
        print("Websocket Connected...")

    # This handler is called when data received from Client
    async def websocket_receive(self, event):
        print("Messaged Received...")

    # This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
    async def websocket_disconnect(self, event):
        print("Websocket Disconnected...")
