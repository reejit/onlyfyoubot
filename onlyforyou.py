from pyrogram import Client
import time

Bot = Client(
     api_id = 1860713,
     api_hash = "c85f4e6137d33c6dad0ca6dd882197ec",
     token = os.environ.get("OK")
)

async def ok(Bot: Bot):
   await Bot.send_message(
       chat_id = -1001696858755,
       text = "fuck you"
   )
   time.sleep(3600)

Bot.run()


