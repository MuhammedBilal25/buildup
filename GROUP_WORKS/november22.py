#write apython program that use while loop to display elements from a given list present at odd index positions
li=[0,1,2,3,4,5,6,7,8,9,10]
i=0
pos=len(li)
while(pos!=0):
    if i%2!=0:
        print(li[i])
    pos-=1
    i+=1
#write a python program that takes input from user and make square list of the numbers and the cube list.Range is 10  number in the list
sq_li=[]
cu_li=[]
for i in range(0,10):
    n=int(input("ENTER THE NUMBER:"))
    sq_li.append(n**2)
    cu_li.append(n**3)
print(f"Square list is: {sq_li}")
print(f"cube list is: {cu_li}")
#pattern print
#1
#1 2 1
#1 2 3 2 1
#1 2 3 4 3 2 1
#1 2 3 4 5 4 3 2 1
for i in range(1,6):
    for c in range(1,i+1):
        print(c,end=" ")
    for k in range(c-1,0,-1):
        print(k,end=" ")
    print()