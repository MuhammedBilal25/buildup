from re import*
text="kaBczabc 9@7c"
pattern="[^a-z]"
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())

