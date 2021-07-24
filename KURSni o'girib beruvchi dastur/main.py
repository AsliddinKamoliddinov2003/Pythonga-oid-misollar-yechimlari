from matn import leng_uz
import requests as r
import json

while True:
    print(leng_uz["main_menu"])
    key=input("manyudan tanlang: ")
    if key=="1":
        usd="https://v6.exchangerate-api.com/v6/980495702019f2beb72d55ac/latest/USD"
        javob=r.get(usd)
        data=json.loads(javob.text)
        print("DOLLAR dan UZB so'miga ☻ ")
        print("Loading...")
        qiymat=int(input("qancha pulni o'girmoqchisiz: "))
        print(data)
        print(data["conversion_rates"]["UZS"]*f"{qiymat}")
    elif key=="2":
        usd="https://v6.exchangerate-api.com/v6/980495702019f2beb72d55ac/latest/USD"
        javob=r.get(usd)
        data=json.loads(javob.text)
        print(data)
        print("DOLLAR dan RUBL ga ☻ ")
        print("Loading...")
        qiymat=int(input("qancha pulni o'girmoqchisiz: "))
        print(data["conversion_rates"]["RUB"]*f"{qiymat}")
    elif key=="3":
        usd="https://v6.exchangerate-api.com/v6/980495702019f2beb72d55ac/latest/UZS"
        javob=r.get(usd)
        data=json.loads(javob.text)
        print("UZB so'midan DOLLAR ga ☻ ")
        print("Loading...")
        qiymat=int(input("qancha pulni o'girmoqchisiz: "))
        print(data["conversion_rates"]["USD"]*f"{qiymat}")
    elif key=="4":
        usd="https://v6.exchangerate-api.com/v6/980495702019f2beb72d55ac/latest/UZS"
        javob=r.get(usd)
        data=json.loads(javob.text)
        print("UZB so'midan RUBL ga ☻ ")
        print("Loading...")
        qiymat=int(input("qancha pulni o'girmoqchisiz: "))
        print(data["conversion_rates"]["RUB"]*f"{qiymat}")
    elif key=="5":
        usd="https://v6.exchangerate-api.com/v6/980495702019f2beb72d55ac/latest/RUB"
        javob=r.get(usd)
        data=json.loads(javob.text)
        print("RUBL dan DOLLAR ga ☻ ")
        print("Loading...")
        qiymat=int(input("qancha pulni o'girmoqchisiz: "))
        print(data["conversion_rates"]["USD"]*f"{qiymat}")
    elif key=="6":
        usd="https://v6.exchangerate-api.com/v6/980495702019f2beb72d55ac/latest/RUB"
        javob=r.get(usd)
        data=json.loads(javob.text)
        print("RUBL dan dan UZB so'miga ☻ ")
        print("Loading...")
        qiymat=int(input("qancha pulni o'girmoqchisiz: "))
        print(data["conversion_rates"]["UZS"]*f"{qiymat}")
    elif key=="#":
        break




                













