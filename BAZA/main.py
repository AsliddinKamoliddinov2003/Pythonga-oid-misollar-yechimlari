main_menu="""
1.Talaba qoshish
2.Talba ochirish
3.Talabani royxatdan korish
#.chiqish"""
first_menu=["Talabani ismini kiriting: ","Talabani yoqtirgan ranginin kiriting: ","Talabani yoqtirgan mashinasini kiriting: "]
second_menu=["TAlabani ID sini kiriting: "]
leng_uz={
    "main_menu": main_menu,
    "first_menu": first_menu,
    "second_menu": second_menu,
    "ask_user":"Menyudan tanlang: ",
    "Error": "dastur yakunlandi kalitda xatolik: "
    }
while True:
    print(leng_uz["main_menu"])
    key=input(leng_uz["ask_user"])
    if key=="#":
        break
    try:
        key=int(key)
    except Exception:
        printr(leng_uz["Error"])
    if key==1:
        name=input(leng_uz["first_menu"][0])
        color=input(leng_uz["first_menu"][1])
        car=input(leng_uz["first_menu"][2])


        
        with open("data.json","a") as file:
            file.write()
        
        