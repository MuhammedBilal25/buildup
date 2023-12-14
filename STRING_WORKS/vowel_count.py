text="pneumonoultramicroscopicsilicovolcanoconiosis"
v_count=0
for ch in text:
    # if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    if ch in ["a","e","i","o","u"]:
        v_count+=1
print(f"vowel count in {text} is {v_count} and total number of letters is {len(text)}")