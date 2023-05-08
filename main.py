import os
import poe

client = poe.Client(os.environ.get("POE_TOKEN"))

for chunk in client.send_message("cheopsbot", "hello"):
    print(chunk["text_new"], end="", flush=True)

for chunk in client.send_message("cheopsbot", "Travel to Cairo for 3 days"):
    print(chunk["text_new"], end="", flush=True)

for chunk in client.send_message("cheopsbot", "Tell me about Lotr"):
    print(chunk["text_new"], end="", flush=True)
