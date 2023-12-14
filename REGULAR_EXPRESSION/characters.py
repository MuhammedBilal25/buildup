from re import*
text="kaBczabc 9@7c"
pattern="[abc]"#a or b or c  [a-e]a to e
matcher=finditer(pattern,text)
count=0
for m in matcher:
    print(m.start(),m.group())
    count+=1
print(count)