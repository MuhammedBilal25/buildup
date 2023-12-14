from re import*
variable_name=input("ENTER THE VARIABLE NAME :")
rule="[a-zA-Z]{1}[a-zA-Z0-9_]*"
matcher=fullmatch(rule,variable_name)
print("invalid" if matcher==None else "valid")