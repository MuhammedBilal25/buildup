# 1. Write a Python program that keep on accepting number from the user until users enter zero display the sum of all number(())
sum=0
while(True):
    num=int(input("ENTER THE NUMBER:"))
    if num!=0:
        sum+=num
    else:
        print(f"SUM OF NUMBERS={sum}")
        break
# 2.Write a python program to accept decimal number and display it’s binary number
decimal=int(input("Enter the decimal number:"))
binary=0
mul=1
while decimal>0:
    rem=decimal%2
    binary=binary+(rem*mul)
    mul=mul*10
    decimal=decimal//2
print(binary)
# 3.Pattern print 
for i in range(6,0,-1):     # 6 6 6 6 6 6 
    for k in range(0,i):    # 5 5 5 5 5 
        print(i,end=" ")    # 4 4 4 4 
    print()                 # 3 3 3 
                            # 2 2 
                            # 1