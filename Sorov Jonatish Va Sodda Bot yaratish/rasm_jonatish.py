import json
import requests as r
from config import BOT_TOKEN

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"
caption=None
def send_photo(chatid, photo_url,caption):
    if caption!=None:
    data = {
        "chat_id":chatid,
        "photo":photo_url,
        "caption":caption,
    }
    r.post(BASE_URL + "sendPhoto", json=data)

rasm="http://images4.fanpop.com/image/photos/22500000/Merlin-merlin-the-young-warlock-22576478-2560-1707.jpg"
send_photo(chatid, rasm)