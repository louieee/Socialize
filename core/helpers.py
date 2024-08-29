from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
def send_ws_signal(data:dict, group:str, message_type:str):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        group,
        {
            'type': message_type,
            'message': json.dumps(data),
        }
    )