matn='bir bor ekam bir yoq ekan bir chol u kampirlkm;kln;kl bolgan ekan'


def fin_min(matn):
    sozlar=matn.split()
    _min=sozlar[0]
    for soz in sozlar:
        if len(_min)>len(soz):
           _min=soz
    return (_min)

print(fin_min(matn))

