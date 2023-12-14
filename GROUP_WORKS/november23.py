# 1. Write a python program to create a list of tuples having first element as the number and second element as the cube of the number
st=int(input("ENTER THE STARTING NUMBER:"))
end=int(input("ENTER THE ENDING NUMBER:"))
lt=[]
for i in range(st,end+1):
    tp=(i,i**3)
    lt.append(tp)
print(lt)
# 2. find the length of the string using for loop
st=input("ENTER THE STRING:")
ct=0
for ch in st:
    ct+=1
print(f"count={ct}")
# 3. Write a program to handling missing keys
dt={"name":"bilal","age":22,"place":"ekm"}
key=input("ENTER THE VALUE:")
if key in dt:
    print("value=",dt.get(key))
else:
    print("VALUE NOT FOUND")
# 4.Pattern print 
ac=65                                           # A 
for i in range(1,6):                        #    B C 
    for k in range(i,5):                    #   D E F 
        print(" ",end="")                   #  G H I J 
    for v in range(1,i+1):              #     K L M N O
        print(chr(ac),end=" ")
        ac+=1
    print() 