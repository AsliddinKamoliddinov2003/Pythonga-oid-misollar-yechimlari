from requests.api import get
from func import send_message,get_updates


menu={
    "keyboard":[
        [{"text":"🍦Buyurtma berish"},{"text":"⏳Buyurtmalarim"}],
        [{"text":"👨🏻‍💻Yordam"},{"text":"⚙️Sozlamalar"}],
        [{"text":"⚽️ O'yinlar"},{"text":"Kontakt","request_contact":True}],
    ],
    "resize_keyboard":True,
    "one_time_keyboard":True,
}

send_message(1220364490,"menyudan tanlang",menu)

data=get_updates()
msg=data[-1]['message']['reply_to_message']['text']
if msg=="🍦Buyurtma berish":
    menu={
        "keyboard":[
            [{"text":"Pizza"},{"text":"Hotdog"},{"text":"lavash"}],
            [{"text":"Pepsi"},{"text":"Coca-cola"},{"text":"RCcola}"}],
        ],
        "resize_keyboard":True,
        "one_time_keyboard":True,
    }
    send_message(1220364490,"Tanlang",menu)