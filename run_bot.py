# run_bot.py
from labot.mitm.bridge import BridgeHandler
from myBot import MyBot
import sys
import os

def run_mitm():
    try:
        from labot.mitm.proxy import create_proxy
        proxy = create_proxy(mybot())
        proxy.start()
    except Exception as e:
        print(f"Error starting MITM: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_mitm()