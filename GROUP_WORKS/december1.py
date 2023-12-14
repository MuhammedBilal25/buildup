# 1. The original list : [1, 3, 5, 1, 3, 2, 5, 4, 2] (user input)
# Matrix after grouping : [[1, 1], [2, 2], [3, 3], [4], [5, 5]]
input_list=[1,3,5,1,3,2,5,4,2]
element_list=[]
matrix_list=[]
count=0
for i in input_list:
    if i not in element_list:
        element_list.append(i)
for i in element_list:
    if input_list.count(i)==2:
        matrix_list.append(list())
        matrix_list[count].append(i)
        matrix_list[count].append(i)
        count=count+1
    elif input_list.count(i)==1:
         matrix_list.append(list())
         matrix_list[count].append(i)
         count=count+1
matrix_list.sort()
print(matrix_list)
#   2.	Write a program to calculate the electricity bill. Accept the number of units consumed from the user
# Unit                        Price
# First 100 units      No charge
# Next 100 units     Rs 5 per unit
# After 200 units    Rs 10 per unit
# For example if input unit is 350 then total bill amount is Rs 2000
unit=int(input("ENTER THE UNIT:"))
price=0
if unit<=100:
    print("NO CHARGE")
elif unit<=200:
    price=(unit-100)*5
    print(f"TOTAL BILL AMOUNT FOR UNIT {unit} IS {price}")
else:
    price=(unit-200)*10+500
    print(f"TOTAL BILL AMOUNT FOR UNIT {unit} IS {price}")
    #    3. Pattern print 
    #   A 
    #  A B 
    # A B C 
#    A B C D 
#   A B C D E
ac=65
for row in range(1,6):
    for space in range(row,6):
        print(end=" ")
    for p in range(0,row):
        print(chr(ac),end=" ")
        ac+=1
    print()
    ac=65

