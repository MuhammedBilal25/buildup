from re import*
text="ab CaK7@#"
# pattern="\d"#[0-9]
# pattern="\D"#[^0-9]
# pattern="\w"#[a-zA-Z0-9]
pattern="\W"#[^a-zA-Z0-9]special characters
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())