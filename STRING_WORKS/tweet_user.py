tweets="What a game , hats off to both teams . Well done @benstokes38 @patcummins30 you have bought test cricket back to life. Love test cricket  @TheBarmyArmy @CricketAus @ECB_cricket"
words=tweets.split(" ")
i=1
print("THE USERS ARE ")
for w in words:
    if w.startswith("@")==True:
        print(f"{i} {w}")
        i+=1

