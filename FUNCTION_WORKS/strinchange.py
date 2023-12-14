text="mobin manoj roshan"
words=text.split(" ")
srt_words=sorted(words,key=lambda w:len(w))
print(srt_words)