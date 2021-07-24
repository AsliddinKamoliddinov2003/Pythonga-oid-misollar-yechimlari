import requests as r
import json
from config1 import BOT_TOKEN
from func import get_updates, send_message
from pprint import pprint

data=get_updates()

len_list = len(data)
Eski_xabar=None
while True:
   
    data = get_updates()
    pprint(data[-1]['message']['text'])
    msg = data[-1]['message']['text']
    chatid = data[-1]['message']['from']['id']
    list=[]
    if len_list != len(data):
       send_message(chatid,"Ismingizni kiriting:")
       print(msg)
       list.append(msg)
       len_list = len(data)
       if len_list!=len(data):
           send_message(chatid,"Familyangizni  kiriting:")
           print(msg)
           list.append(msg)
           len_list = len(data)
        Eski_xabar=data[-1]['message']['text']

with open("malmot.json",'w') as file:
    data={
        "messeges":list
    }
    json.dump(data,file)

# {'message': {'chat': {'first_name': '𝐴𝑆𝐿𝐼𝐷𝐷𝐼𝑁',
#                       'id': 1220364490,
#                       'type': 'private',
#                       'username': 'asl1dd1n10beckend'},
#              'contact': {'first_name': '𝐴𝑆𝐿𝐼𝐷𝐷𝐼𝑁',
#                          'phone_number': '998995223101',
#                          'user_id': 1220364490},
#              'date': 1622678564,
#              'from': {'first_name': '𝐴𝑆𝐿𝐼𝐷𝐷𝐼𝑁',
#                       'id': 1220364490,
#                       'is_bot': False,
#                       'language_code': 'uz',
#                       'username': 'asl1dd1n10beckend'},
#              'message_id': 112,
#              'reply_to_message': {'chat': {'first_name': '𝐴𝑆𝐿𝐼𝐷𝐷𝐼𝑁',
#                                            'id': 1220364490,
#                                            'type': 'private',
#                                            'username': 'asl1dd1n10beckend'},
#                                   'date': 1622678553,
#                                   'from': {'first_name': 'Kimsan bot',
#                                            'id': 1701058934,
#                                            'is_bot': True,
#                                            'username': 'lkdnscvknsd_bot'},
#                                   'message_id': 111,
#                                   'text': 'menyudan tanlang'}},
#  'update_id': 95520465