def poli(soz ,flag=False):

    if len(soz)<2:
        return flag
    if soz[0]==soz[-1]:
        flag=True
    else:
        flag= False
    return poli(soz[1:-1], flag=flag)

print(poli('non'))
