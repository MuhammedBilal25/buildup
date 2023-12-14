# 1. Write a Python program that ask users to enter a number and keep asking the users to enter a correct number, until the number with in the range that we given
while True:
    user_input = int(input(f"Enter a number between 1 and 5: "))
    if 1 <= user_input <= 5:
        print(f"You entered a valid number: {user_input}")
        break
    else:
        print(f"Number out of range. Please enter a number between 1 and 5.")
# 2.Write a python program to list the even numbers from the range that given by the user and delete the multiplication of 5 from the list
num_lst=[]
start=int(input("ENTER THE NUMBBER TO START FROM:"))
stop=int(input("ENTER THE NUMBBER TO END:"))
for i in range(start,stop+1):
    if i%2==0:
        num_lst.append(i)
print(f"even numbers between {start}and{stop} are {num_lst}")
for n in num_lst:
    if n%5==0:
        num_lst.remove(n)
print(f"result={num_lst}")
# 3.Pattern print 
for i in range(1,6):        #                         *
    for k in range(i,5):    #                       *   *
        print(" ",end="")   #                     *   *  *
    for w in range(0,i):    #                   *  *   *   *
        print("*",end=" ")  #                 *   *   *   *   *
    print()                 #                 *   *   *   *   *
for i in range(1,6):        #                   *  *   *   *
    for k in range(i,1,-1): #                     *   *  *
        print(" ",end="")   #                       *   *
    for w in range(6,i,-1): #                         *
        print("*",end=" ")
    print()