# mybot.py
from labot.mitm.bridge import BridgeHandler
from labot.data.msg import Msg
import labot.protocol

class MyBot(BridgeHandler):
    def handle_message(self, source, msg):
        try:
            msg_type = msg.msgType
            msg_json = msg.json()
            
            # Handle specific message types
            if msg_type == "ChatServerMessage":
                print(f"Chat message received: {msg_json}")
            elif msg_type == "GameMapMovementMessage":
                print(f"Movement detected: {msg_json}")
            
            # Always forward messages
            if source == "client":
                self.send_to_server(msg)
            else:
                self.send_to_client(msg)
                
        except Exception as e:
            print(f"Error: {e}")
    
    # Function to send chat message
    def send_chat(self, content):
        chat_msg = {
            "__type__": "ChatClientMultiMessage",
            "content": content,
            "channel": 0
        }
        self.send_to_server(Msg.from_json(chat_msg))

if __name__ == "__main__":
    bot = MyBot()