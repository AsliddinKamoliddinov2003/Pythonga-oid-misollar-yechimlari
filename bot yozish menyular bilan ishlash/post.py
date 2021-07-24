import requests as r
import json
from config1 import BOT_TOKEN


url = f"https://api.telegram.org/bot{BOT_TOKEN}/"
Update_url=url+"getUpdates"

javob = r.get(url)
data = json.loads(javob.text)

len_list = len(data)


while True:
    javob = r.get(Update_url)
    print(javob)
    data = json.loads(javob.text)
    msg = data['result'][-1]['message']['text']
    chatid = data['result'][-1]['message']['from']['id']
    if len_list != len(data['result']):
        send_message=url+"sendMessage"
        r.post(send_message,json={"chat_id":chatid,"text":"salom"})
        print(msg)
        len_list = len(data['result'])