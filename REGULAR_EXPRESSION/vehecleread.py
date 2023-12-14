from re import*
f=open("C:\\Users\\USER\\Desktop\\L-P\\REGULAR_EXPRESSION\\vehecle_numbers.txt","r")
rule="((KL)|(TN)){1}(-)?\d{2}(-)?[A-Z]{1,2}(-)?\d{4}"
for line in f:
    vehicle_no=line.rstrip()
    matcher=fullmatch(rule,vehicle_no)
    if matcher!=None:
        print(vehicle_no)