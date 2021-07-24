matn='bir bor Ekam bir yoq ekan bir chol u kampirlkm;kln;kl bolgan ekan'


sozlar=matn.split()
takror={}
for soz in sozlar:
    if soz in takror:
        takror[soz]+=1
    else:
        takror[soz]=1

print(takror)