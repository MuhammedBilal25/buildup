dengue=["ekm","ekm","tsr","tvm","tvm","ekm","tvm","edk","tvm"]
dengu_dic={}
for w in dengue:
    if w in dengu_dic:
        dengu_dic[w]+=1
    else:
        dengu_dic[w]=1
print(dengu_dic)
srt_dengu=sorted(dengu_dic,key=lambda k:dengu_dic.get(k),reverse=True)
print(srt_dengu)
print(srt_dengu[0])