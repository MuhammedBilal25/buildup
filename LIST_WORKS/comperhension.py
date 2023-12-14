lst=[2,4,5,6,7,8,9]
squares=[]
for num in lst:
    sq=num**2
    squares.append(sq)
print(squares)
even=[]
for num in lst:
    if num%2==0:
        even.append(num)
print(even)
# [return value for num in lst condition]
square=[num**2 for num in lst]
print(square)
cube=[num**3 for num in lst]
print(cube)
even= [ num for num in lst if num%2==0]
print(even) 


