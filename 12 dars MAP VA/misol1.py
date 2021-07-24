matn='bir bor ekam bir yoq ekan bir chol u kampirlkm;kln;kl bolgan ekan'


def fin_max(matn):
    sozlar=matn.split()
    _max=sozlar[0]
    for soz in sozlar:
        if len(_max)<len(soz):
           _max=soz
    return (_max)

print(fin_max(matn))

