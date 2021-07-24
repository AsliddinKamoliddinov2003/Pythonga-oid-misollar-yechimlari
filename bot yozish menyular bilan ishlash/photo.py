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

def send_message(chatid,photo_url):
    data={
        "chat_id":chatid,
        "photo":photo_url
    }
    rasm="https://www.google.com/imgres?imgurl=https%3A%2F%2Fimg.championat.com%2Fs%2F735x490%2Fnews%2Fbig%2Fi%2Fb%2Flionel-messi-obognal-pele-po-golam-za-odin-klub_1608716553651652193.jpg&imgrefurl=https%3A%2F%2Fwww.championat.com%2Ffootball%2Farticle-4224177-napadayuschij-barselony-lionel-messi-obognal-pele-po-golam-za-odin-klub.html&tbnid=il4akQ3JaHb0cM&vet=12ahUKEwjYw4rlmfnwAhVMySoKHX0VBtUQMygAegUIARC3AQ..i&docid=DJeUjLB5S5Ri9M&w=735&h=490&q=messi&ved=2ahUKEwjYw4rlmfnwAhVMySoKHX0VBtUQMygAegUIARC3AQ"
    r.post(url+"sendMessage",rasm)
