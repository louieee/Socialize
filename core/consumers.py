from channels.generic.websocket import AsyncWebsocketConsumer
import json

class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'your_group_name'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Handle incoming data here
        
        # Send a message back to the client
        await self.send(text_data=json.dumps({
            'message': 'Received your data',
        }))

    async def send_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
