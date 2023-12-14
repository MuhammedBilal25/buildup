from re import*
variable_name=input("ENTER THE VARIABLE NAME :")
rule="[k-nK-N][369]\w*"
matcher=fullmatch(rule,variable_name)
print("invalid" if matcher==None else "valid")
