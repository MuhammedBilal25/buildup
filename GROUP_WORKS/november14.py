# 1. Write a Python program that separate positive and negative numbers from a list
number_list=[1,2,0,-2,-3,2,45,-39]
positive_number=[]
negative_number=[]
for n in number_list:
    if n>=0:
        positive_number.append(n)
    else:
        negative_number.append(n)
print(f"{positive_number} are positive numbers\n{negative_number} are negative numbers")
# 2.Write a python program to reverse the tuple
tp=(10,28,79,8,3,0,38)
tplst=[]
for i in range(len(tp)-1,-1,-1):
    tplst.append(tp[i])
reverse_tuple=tuple(tplst)
print(f"{tp} after reverse is {reverse_tuple}")
# 3.Pattern print
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3 
# 4 4  
# 5
for i in range(1,6):
    for k in range(i,6):
        print(i,end=" ")
    print()
