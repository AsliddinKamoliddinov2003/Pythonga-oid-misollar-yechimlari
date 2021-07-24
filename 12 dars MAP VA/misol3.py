matn='bir bor ekam bir yoq ekan bir chol u kampirlkm;kln;kl bolgan ekan'

sozlar=matn.split()
_max=sozlar[0]
_max=sozlar[0].count('a')
for soz in sozlar:
    if _max<soz.count('a'):
        _max=soz
        _max=soz.count('a')
print(_max,soz)



