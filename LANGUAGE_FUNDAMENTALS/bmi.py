weight=int(input("WEIGHT IN KG = "))
height=int(input("HEIGHT IN CM ="))
h_m=height/100
bmi=weight/(h_m**2)
print(f"BMI OF WEIGHT {weight}KG and height {height}m is {bmi} ")