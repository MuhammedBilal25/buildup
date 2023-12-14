from re import *

pan_card=input("enter  pan card number:")

rule="[A-Z]{3}(-)?[PCAFHT](-)?[A-Z](-)?[0-9]{4}(-)?[A-Z]"

matcher=fullmatch(rule,pan_card)

print("invalid" if matcher==None else  "valid")