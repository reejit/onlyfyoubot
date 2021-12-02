from pyrogram import Client
import time
import os

Bot = Client(
     api_id = 1860713,
     api_hash = "c85f4e6137d33c6dad0ca6dd882197ec",
     bot_token = os.environ.get("OK"),
     session_name = ":memory:"
)


Bot.run()
while True:
    Bot.send_message(
       chat_id = -1001696858755,
       text = "fuck you"
    )
    print ("sent")
    time.sleep(3600)
    print ("sleep")



