import requests as r
import json
from config import bot_token
from datetime import datetime
from time import time 

UPDATE_URL=f'https://api.telegram.org/bot1701058934:AAHo96SuEaI90GyiiLTNtSrlo4I5tWXlFiI/getUpdates'

eski_matn=None

while True:
    response=r.get(UPDATE_URL)
    response_dic=json.loads(response.text)
    print(response_dic)
    msg=response_dic["result"][-1]["message"]["text"]
    if eski_matn!=msg:
        print(msg)

    eski_matn=msg

# response=r.get(UPDATE_URL)
# response_dic=json.loads(response.text)
# vaqt=response_dic["result"][-1]["message"]["data"]
# ID=response_dic["result"][-1]["message"]["chat"]["id"]
# dt= datetime.fromtimestamp(vaqt)
# chasa="{}:{}:{}".format(dt.hour,dt.minute,dt.second)
# print(ID)
# print(chasa)

    


# with open("data.json","a") as file:
#     data={
#         "User_id":ID,
#         "vaqt":chasa,
#         "matn":eski_matn,
#         }
    




   
