# 1.Write a program to print 10,8,6,4,2,0,-2,-4,-6,-8,-10
for i in range(10,-12,-2):
    print (i)
# 2. Write a program to print sum of even number in a range
start=int(input("ENTER THE START RANGE:"))
limit=int(input("ENTER THE END RANGE:"))
sum=0
for i in range(start,limit+1):
    if i%2==0:
        sum+=i
print(f"sum of even numbers from {start} to {limit} is {sum} ")
# 3. Write a program to calculate BMI and give message ‘’over weight,underweight,healthy’’
weight=int(input("WEIGHT IN KG = "))
height=int(input("HEIGHT IN CM ="))
h_m=height/100
bmi=weight/(h_m**2)
print(f"BMI OF WEIGHT {weight}KG and height {height}m is {bmi}")
if bmi<19:
    print("you are under weight")
elif bmi<25:
    print("you are HEALTHY")
elif bmi>=25:
    print("you are OVER WEIGHT")  
