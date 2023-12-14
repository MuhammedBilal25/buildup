# 1.Write a python program to find factorial of a prime number
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(f"factorial of {num} is {fact}")
num=int(input("enter prime number:"))
for i in range(2,num):
    if num%i==0:
        print(f"{num} is not prime")
        break
else:
    factorial(num)
# 2.Write a python program to display Fibonacci series and specify that number odd or even
limit=int(input("ENTER THE LIMIT:"))
pre=0
cur=1
if limit==1:
    print(f"{pre}-zero")
elif limit==2:
    print(f"{pre}-zero,{cur}-odd")
elif limit>2:
    print(f"{pre}-zero,{cur}-odd",end=",")
    for i in range(1,limit-1):
        next=pre+cur
        if next%2==0:
            print(f"{next}-even",end=",")
        else:
            print(f"{next}-odd",end=",")
        pre=cur
        cur=next
else:
    print("INVALID INPUT!")
# 3.Write a python program to reverse digits in a number
num1=int(input("\nENTER THE NUMBER :"))
while num1!=0:
    last_digit=num1%10
    print(last_digit,end="")
    num1=num1//10