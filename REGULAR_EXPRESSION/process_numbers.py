from re import*
f=open("C:\\Users\\USER\\Desktop\\L-P\\REGULAR_EXPRESSION\\numbers.txt","r")
rule="([+]91)?(-)?[0-9]{10}"
for num in f:
    number=num.rstrip("\n")
    matcher=fullmatch(rule,number)
    if matcher!=None:
        print(number)