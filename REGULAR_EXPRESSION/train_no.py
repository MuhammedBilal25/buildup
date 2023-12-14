from re import *
f=open("C:\\Users\\USER\\Desktop\\L-P\\REGULAR_EXPRESSION\\news.txt")
rule="[0-9]{5}"
for line in f:
    number=line.rstrip("\n")
    # #####
    matcher=finditer(rule,number)
    for m in matcher:
        print(m.group())
    # #####
    # num=line.split(" ")
    # for n in num:
    #     matcher=fullmatch(rule,n)
    #     if matcher!=None:
    #         print(n)