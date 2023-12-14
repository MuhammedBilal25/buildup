lst=["red","green","blue","white","black","apple","ignore","under"]
#q1 print words starting with vowels
#q2 print words starting with consonants
#vowel_words=[]
#consonent_words=lst.copy()
#vowels=["a","e","i","o","u"]
#for word in lst:
#    for vow in vowels:
#        if word.startswith(vow):
#            vowel_words.append(word)
#            consonent_words.remove(word)
vowel_words=[w for w in lst if w[0] in ["a","e","i","o","u"]]
consonent_words=[w for w in lst if w[0] not in ["a","e","i","o","u"]]
print(f"WORDS STARTING WITH VOWELS ARE : {vowel_words}")
print(f"WORDS STARTS WITH CONSONENTS ARE : {consonent_words}")