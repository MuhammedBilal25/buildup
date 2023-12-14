num=input("ENTER THE NUMBER = ")
digit_count=len(num)
num=int(num)
temp=num
sum=0
while (num!=0):
    digit=num%10
    exp=digit**digit_count
    sum=sum+exp
    num=num//10
print(sum)
print("IS AN ARMSTRONG" if temp==sum else "NOT AN ARMSTRONG")