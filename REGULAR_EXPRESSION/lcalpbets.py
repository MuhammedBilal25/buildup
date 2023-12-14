from re import*
text="kaBczabc 9@7c"
pattern="[A-Za-z0-9]"#lowercase a to z and uppercase A to Z and 0 to 9
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())