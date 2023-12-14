from re import*
month=input("ENTER THE MONTH(MM):")
rule="(0[1-9]|1[0-2])"
matcher=fullmatch(rule,month)
print("invalid" if matcher==None else "valid")