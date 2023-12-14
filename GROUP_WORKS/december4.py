# 1. Write a python program to identify unique triplets whose three elements sum to zero from an array of n integers
arry_lst=[1,-2,3,4,-5,6,7,8,-9,-10]
triplelet_list=[]
c=0
triplelet_set=set()
for i in arry_lst:
    for k in arry_lst:
        t=-(i+k)
        if t in arry_lst:
            temp_list=[i,k,t]
            temp_list.sort()
            while temp_list not in triplelet_list:
                triplelet_list.append(list())
                triplelet_list[c].append(i)
                triplelet_list[c].append(k)
                triplelet_list[c].append(t)
                triplelet_list[c].sort()
                c+=1
print(f"the triplets whose sum is zero are {triplelet_list}")               
# 2. Write a python program to make combinations of 3 digits
num_list=[1,2,3,4,5]
num_set=set()
for i in num_list:
    for k in num_list:
        for j in num_list:
            num=i*100+j*10+k
            num_set.add(num)
print(num_set)
# 3. Pattern print 
    # *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *
print("      *")
for i in range(1,5):
    for k in range(i,5):  
        print(" ",end="")
    print("*",end=" ")
    for j in range(0,i):
        print(" ",end=" ")
    print("*")
for i in range(1,7):      
    for k in range(i,1,-1):                   
        print(" ",end="")
    print("*",end=" ")                    
    for w in range(6,i,-1):                       
        print(" ",end=" ")
    print("*")
print("      *")


 
