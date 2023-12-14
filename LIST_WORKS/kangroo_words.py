source_word="myself"
target_word="self"
source_word_list=[ch for ch in source_word]
target_word_list=[ch for ch in target_word]
print(target_word_list)
for ch in target_word_list:
    if ch in source_word_list:
        source_word_list.remove(ch)
    else:
        print("NOT A KANGROO WORD")
        break
else:
    print("IS A KANGROO WORD")
