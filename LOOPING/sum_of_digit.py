num=int(input("ENTER THE NUMBER :"))
sum=0
while num!=0:
    last_digit=num%10
    print(last_digit)
    sum=sum+last_digit
    num=num//10
print(f"SUM = {sum}")