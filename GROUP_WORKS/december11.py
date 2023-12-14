# 1. Write a Python program to find the second largest number in a list.
li=[1,43,5,4,56,3]
li.sort(reverse=True)
print(f"second largest elemrnt is:{li[1]}")
# 2. Write a program to filter the dictionary, from a dictionary of people’s heights and you wanted to filter out anyone below a certain height.Let’s filter out anyone less than 170cm.
height={
    "A":112,
    "B":187,
    "C":190,
    "D":199,
    "E":173,
    "F":166
}
for k in height:
    if height.get(k)<170:
        print(f"{k}-{height.get(k)}cm")
    
# 3. Pattern print
num=4                                                           # 4 4 4 4 4 4 4  
for row in range(1,8):                                          # 4 3 3 3 3 3 4   
   for col in range(1,8):                                       # 4 3 2 2 2 3 4   
        print(max(row-3,col-3,2*num-col-3,2*num-row-3),end=" ") # 4 3 2 1 2 3 4   
   print()                                                      # 4 3 2 2 2 3 4   
                                                                # 4 3 3 3 3 3 4   
                                                                # 4 4 4 4 4 4 4                            
