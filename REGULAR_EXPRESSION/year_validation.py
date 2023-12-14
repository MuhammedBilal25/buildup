from re import*
year=input("ENTER THE YEAR(YYYY):")
rule="(19|20)[0-9]{2}"
matcher=fullmatch(rule,year)
print("invalid" if matcher==None else "valid")