text="#@12pneumonoultramicroscopicsilicovolcanoconiosis"
c_count=0
for ch in text:
    if ch  not in ["a","e","i","o","u"] and ch.isalpha():
        c_count+=1
print(f"consonent count in {text} is {c_count} and total number of letters is {len(text)}")
