import poe
from poe import Client
import json

class PoeChatBot:

    def __init__(self,token):
        self.token = token

    def get_client(self)->Client:
        client = poe.Client(self.token)
        return client
    
    def get_bot_names(self):
        bot_names = json.dumps(self.get_client().bot_names)
        return bot_names

    def chat(self, bot, content):
        client = self.get_client()
        try:
            yield from client.send_message(bot, content, with_chat_break=True, timeout=15)
        except Exception as e:
            print(f"Chat error: {e}")
            client.disconnect_ws()


