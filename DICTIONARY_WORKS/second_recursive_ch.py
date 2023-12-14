text="ABCABD"
chc={}
chcl=[]
for ch in text:
    if ch in chc:
        chc[ch]+=1
        chcl.append(ch)
    else:
       chc[ch]=1
print(ch)
print(chcl[1])