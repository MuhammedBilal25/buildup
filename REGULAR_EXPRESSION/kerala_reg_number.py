from re import*
vehicle_no=input("ENTER VEHICLE NUMBER:")
rule="(KL){1}(-)?\d{2}(-)?[A-Z]{1,2}(-)?\d{4}"
matcher=fullmatch(rule,vehicle_no)
print("invalid" if matcher==None else "valid")