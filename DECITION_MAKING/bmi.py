weight=int(input("WEIGHT IN KG = "))
height=int(input("HEIGHT IN CM ="))
h_m=height/100
bmi=weight/(h_m**2)
print(f"BMI OF WEIGHT {weight}KG and height {height}m is {bmi} ")
if bmi<19:
    print("you are under weight")
elif bmi<25:
    print("you are HEALTHY")
elif bmi<30:
    print("you are OVER WEIGHT")
elif bmi<40:
    print("you are obese")
elif bmi>=40:
    print("you are severe obese")

     
    