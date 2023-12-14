items=["bat","ball","stumps","helmet","arc","cricketball"]
# longest_word=max(items,key=lambda w:len(w))
# print(f"LONGEST WORD={longest_word}")
# min_WOR=min(items,key=lambda w:len(w))
# print(f"SHORTEST WORD = {min_WOR}")
sum=0
for i in range(0,len(items)):
    sum=len(items[i])+sum
print(sum)

largest_word=items[0]
for i in range(1,len(items)):
    if len(items[i])>len(largest_word):
        largest_word=items[i]
print(largest_word)

minimum_word=items[0]
for i in range(1,len(items)):
    if len(items[i])<len(minimum_word):
        minimum_word=items[i]
print(minimum_word)
