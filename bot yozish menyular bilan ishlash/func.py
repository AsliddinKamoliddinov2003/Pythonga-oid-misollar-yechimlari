import requests as r
import json
from config1 import BOT_TOKEN


url = f"https://api.telegram.org/bot{BOT_TOKEN}/"
Update_url=url+"getUpdates"

javob = r.get(url)
data = json.loads(javob.text)

def get_updates():
    javob = r.get(Update_url)
    return json.loads(javob.text)["result"]

def send_message(chatid,text):
    data={
        "chat_id":chatid,
        "text":text,
        # "reply_markup":menu,
    }
    r.post(url+"sendMessage",json=data)
