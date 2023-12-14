# 1,Write a Python program that accepts a string and calculates the number of digits and letters.
string=input("ENTER THE STRING:")
ac=0
nc=0
for ch in string:
    if ch.isalpha()==True:
        ac+=1
    elif ch.isdigit()==True:
        nc+=1
print(f"there are {nc} number of digits and {ac} number of alphabets in ' {string} '")
# 2.Write a python program to display multiplication table of a number (user input)
n=int(input("ENTER THE NUMBER:"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")
# 3.Pattern print
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5
for i in range(1,6):
    for k in range(0,i):
        print(i,end=" ")
    print()