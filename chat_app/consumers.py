import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

import datetime
import pytz

tz = pytz.timezone('Asia/Kolkata')


class ChatConsumer(WebsocketConsumer):
    #Handle Connect
    def connect(self):
        self.user = self.scope['user']
        self.room_group_name = self.scope['url_route']['kwargs']['room_name']

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        if self.user.is_anonymous:
            self.close()
        else:
            self.accept()

    #Handle disconnect
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        self.close()

    #Receives message from socket and broadcasts in the group
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'send_message',
                'message':message,
            }
        )

    #Receives message from the group and sends to the socket
    def send_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'message': message
        }))