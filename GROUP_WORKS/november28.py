# 1. Write a python program to find the sum of elements in a tuple
tp=(10,80,7,8,9,6)
print(f"THE SUM IS:{sum(tp)}")
# 2.Convert tuple to a list and find sum
tp=(1,10,8,40,11)
tp_list=list(tp)
print(f"THE SUM IS:{sum(tp_list)}")
# 3. Pattern print 
# A 
# B B 
# C C C 
# D D D D 
# E E E E E
ac=65
for i in range(1,6):
    for k in range(0,i):
        print(chr(ac),end=" ")
    ac+=1
    print()
