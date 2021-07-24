import requests as r 
import json

url="https://v6.exchangerate-api.com/v6/980495702019f2beb72d55ac/latest/USD"
javob = r.get(url)
data=json.loads(javob.text)
with open("data.json","w") as file:
    data={
        "COUNTRY_SHORT_VERSION": list(data["conversion_retes"].keys())
        }

    json.dump(data,file)
