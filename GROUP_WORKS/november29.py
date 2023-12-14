# 1.Write a nested for loop program to print multiplication table 
for i in range(1,11):
    for k in range(1,11):
        print(i*k,end=" ")
    print()
# 2.Print the output in multiple raw
name=input("ENTER YOUR NAME: ")
rg=int(input("ENTER THE RANGE: "))
for i in range(1,rg+1):
    print(name)
# Pattern print 
for i in range(1,8):            #1 1 1 1 1 1 1
    for k in range(i,8):        #2 2 2 2 2 2
        print(i,end=" ")        #3 3 3 3 3 
    print()                     #4 4 4 4 
                                #5 5 5
                                #6 6
                                #7

