def oy_sonlari(n=28):
    for kun in range(1,n+1):
        print(kun)
def oy_nomlari(k):
    if k==1:
        print('yanvar')
        oy_sonlari(31)
    if k==2:
        print('Fevral')
        oy_sonlari(28)
    if k==3:
        print('Mart')
        oy_sonlari(31)
    if k==4:
        print('Aprel')
        oy_sonlari(31)
    if k==5:
        print('May')
        oy_sonlari(31)
    if k==6:
        print('Iyun')
        oy_sonlari(31)
    if k==7:
        print('Iyul')
        oy_sonlari(30)
    if k==8:
        print('Avgust')
        oy_sonlari(31)
    if k==9:
        print('Sentyabr')
        oy_sonlari(31)
    if k==10:
        print('Oktyabr')
        oy_sonlari(30)
    if k==11:
        print('Noyabr')
        oy_sonlari(30)
    if k==12:
        print('Dekabr')
        oy_sonlari(31)
oy_nomlari(7)