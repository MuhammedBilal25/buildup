# 1. Create a program to print all the numbers in the range 10-50 excluding the multiples of 2 and 3 
for i in range(10,51):
    if i%2!=0 and i%3!=0:
        print(i)
# 2. Python program to check if the given string is a palindrome.
string=input("ENTER THE STRING : ")
st=string.lower()
lst=[]
rev="" 
for ch in st:
   lst.append(ch)
lst.reverse()            #rev_string = my_string[::-1]
for i in lst:
    rev+=i
print(f"reverse of {string} is {rev}")
if rev==st:
    print("therefor the given string is palindrome")
else:
    print("therefor the given string is NOT palindrome")
# 3. Pattern print 
for i in range(1,6):         #    1 1 1 1 1 1 1
    for k in range(0,6):     #    2 2 2 2 2 2 2
        print(i,end=" ")     #    3 3 3 3 3 3 3 
    print()                  #    4 4 4 4 4 4 4
                             #    5 5 5 5 5 5 5