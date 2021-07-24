matn='bir bor Ekam bir yoq ekan bir chol u kampirlkm;kln;kl bolgan ekan'

sozlar=matn.split()
sanoq=0
for soz in sozlar:
    if soz.istitle():
        sanoq+=1
print(sanoq)
