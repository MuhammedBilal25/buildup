f=open("C:\\Users\\USER\\Desktop\\L-P\\FILE_INPUT_OUTPUT\\news.txt","r")
for line in f:
    word=line.rstrip("\n").split(" ")
    print(word)