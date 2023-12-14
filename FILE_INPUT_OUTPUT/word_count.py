f=open("C:\\Users\\USER\\Desktop\\L-P\\FILE_INPUT_OUTPUT\\news.txt","r")
wc={}
for line in f:
    word=line.rstrip("\n").split(" ")
    for w in word:
        if w in wc:
            wc[w]+=1
        else:
            wc[w]=1
print(wc)