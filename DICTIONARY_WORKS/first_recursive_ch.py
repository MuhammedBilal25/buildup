text="ABCABBDE"
chc={}
for ch in text:
    if ch in chc:
        chc[ch]+=1
        break
    else:
       chc[ch]=1
print(ch) 
