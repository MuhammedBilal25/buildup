text="ABCABBDE"
chc={}
for ch in text:
    if ch in chc:
        chc[ch]+=1
    else:
       chc[ch]=1
for k,v in chc.items():
    if (v==1):
        print(k)