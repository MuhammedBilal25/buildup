from re import*
num=input("ENTER THE NUMBER:")
rule="[+]{1}[1]{1}[0-9]{10}"
matcher=fullmatch(rule,num)
print("invalid" if matcher==None else "valid")