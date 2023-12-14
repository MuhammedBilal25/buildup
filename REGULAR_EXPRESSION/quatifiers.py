from re import*
text="aaabcaabbaaaabd"
# pattern="a*"#any number of a including 0
# pattern="a{2}"#two number of a 
pattern="a{2,4}"#2 to 4 numbers of a
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())