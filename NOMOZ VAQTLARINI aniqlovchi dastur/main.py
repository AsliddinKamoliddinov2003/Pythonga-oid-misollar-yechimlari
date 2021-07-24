import requests as r
import json
from pprint import pprint 

while True:
    print("Loading...")
    joy_nomi=input("joy nomini kiriting: ")
    url=f"https://api.pray.zone/v2/times/today.json?city={joy_nomi}"

    javob=r.get(url)

    data=json.loads(javob.text)

    pprint(data["results"]["datetime"][0]["times"])
    ushlab_tur=input("n: ")