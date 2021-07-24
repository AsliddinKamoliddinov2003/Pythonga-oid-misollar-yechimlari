from flask import Flask

app = Flask(__name__)

Qoshiqchilar=[
    {"id":1,"name":"Gafur","davlat":"Uzbekistan"},
    {"id":2,"name":"Rauf va Faik","davlat":"Rossiya"},
    {"id":3,"name":"Ramil","davlat":"Rossiya"},
    {"id":4,"name":"Ulug;bek Rahmatullayev","davlat":"Uzbekistan"},
    {"id":5,"name":"Serebro guruh","davlat":"Rossiya"},
    {"id":6,"name":"Jony","davlat":"Azarbaijan"},
    {"id":7,"name":"MBAND gurub","davlat":"Rossiya"},
    {"id":8,"name":"Anivar","davlat":"Rossiya"},
    {"id":9,"name":"Bruno Mars","davlat":"AQSH"},
    {"id":10,"name":"Jan Khalib","davlat":"Rossiya"},
    
]


@app.route("/")
def bosh_sahifa():
    text=""
    for pesnya in Qoshiqchilar:
        text += str(pesnya["id"])+":" + pesnya["name"] + ":" + pesnya["davlat"]
        text += "<br>"
    return text
@app.route("/<id>/")
def Yakka(id):
    tanlangan=(list(filter(lambda person: person["id"]==int(id),Qoshiqchilar)))

    text=""

    for pesnya in tanlangan:
        text += str(pesnya["id"])+":" + pesnya["name"] + ":" + pesnya["davlat"]
        text += "<br>"
    return text
@app.route("/<id>/deleta/")
def qolganlari(id):
    tanlangan=(list(filter(lambda person: person["id"]!=int(id),Qoshiqchilar)))

    text=""

    for pesnya in tanlangan:
        text += str(pesnya["id"])+":" + pesnya["name"] + ":" + pesnya["davlat"]
        text += "<br>"
    return text
@app.route("/<year>/<month>/<day>/")
def kun(year,month,day):
    return f"{year}:{month}:{day}"



app.run(debug=True)