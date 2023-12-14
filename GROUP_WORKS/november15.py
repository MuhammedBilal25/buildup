# 1. Write a Python program to find n natural number in ascending order
n=int(input("ENTER THE LIMIT:"))
for i in range(1,n+1):
    print(i,end=" ")
# 2.Write a python program to find n natural number in descending order
m=int(input("ENTER THE LIMIT:"))
for i in range(m,0,-1):
    print(i,end=" ")
# 3.Pattern print 
        # * 
    #   * * 
    # * * * 
#   * * * * 
# * * * * *
print()
for i in range(1,6):
    for k in range(i,5):
        print(" ",end=" ")
    for w in range(0,i):
        print("*",end=" ")
    print()
    