# 1. Write a Python program that print 2 list and common element
lst1=[1,3,5,6,4,7]
lst2=[2,7,0,8,9,5]
set1=set(lst1)
set2=set(lst2)
common=set1.intersection(set2)
common_lst=list(common)
print(f"list 1 is {lst1}\nlist 2 is {lst2}]\ncommon elements is {common_lst}")
# 2.Write a python program to find the least square number from a list
lst=[2,9,25,54,7]
lst.sort()
print(f"the list is{lst}")
for n in lst:
    sq_rt=n**0.5
    zero=sq_rt-int(sq_rt)
    if zero==0.0:
        print(f"least square number is {n}")
        break   
# 3.Pattern print 
for i in range(1,6) :                       # 1
    for k in range(1,i+1):                  # 1 2 
        print(k,end=" ")                    # 1 2 3 
    print()                                 # 1 2 3 4 
                                            # 1 2 3 4 5
