num=int(input("ENTER THE NUMBER : "))
sum=0
while num!=0:
    digit=num%10
    digit_cube=digit**3
    sum=sum+digit_cube
    num=num//10
print(sum)