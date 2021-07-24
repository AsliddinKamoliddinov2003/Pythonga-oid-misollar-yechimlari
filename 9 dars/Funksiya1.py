def Royxat(ism,Tugilgan_yil):
    let = 2021 - Tugilgan_yil
    print(f'ism = {ism.title()}\n yosh={let}')

    if 4<=let<7:
        print('siz bogchada talim olasiz')
    elif 7<=let<=18:
        print('siz maktabda talim olasiz')
    elif 18<=let<30:
        print('siz oliy oquv yurtida talim olasiz') 
    elif 1 <= let < 4:
        print('siz hali bolasiz')
    else:
        print('Bekorchisiz')

return lambda()
    