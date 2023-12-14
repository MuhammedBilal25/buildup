# 1. Write a Python program to find leap year (user input)
year=int(input("ENTER THE YEAR:"))
if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
# 2.Write a python program to sum all the items in the dictionary 
dict={
    "rohit": 45,
    "virat":18,
    "surya":63,
    "sreyas":96,
    "jadeja":8,
    "klrahul":1
}
sum=0
for d in dict:
    sum=sum+dict[d]
print(f"the sum is {sum}")
# 3.Pattern print 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *
for i in range(0,5):
    for k in range(0,5):
        print("*",end=" ")
    print()