#1.Write a program to display ‘’HELLO’’ if a number 
# entered by user is a multiple of five, otherwise print ‘’Bye"
num=int(input("ENTER THE NUMBER:"))
print("HELLO" if num%5==0 else "Bye")
# 2.Write a program to check whether a person is eligible for voting or not
age=int(input("ENTER YOUR AGE:"))
print("eligible" if age>=18 else "not eligible")

# 3.Write a program to accept percentage from the user and display the grade according to the following criteria:
# Mark > 90 =A Grade
# >80 and <= 90 = B Grade
# >=60 and <= 80 =C Grade
# Below 60 = D grade

mark=int(input("ENTER THE MARK PERCENTAGE:"))
if mark>90:
    print("A Grade")
elif mark>80:
    print("B Grade")
elif mark>=60:
    print("C grade")
else:
    print("D grade")

# 4.Write a program to find the largest number out of three numbers excepted from user.

num1=int(input("ENTER THE NUMBER1: "))
num2=int(input("ENTER THE NUMBER2: "))
num3=int(input("ENTER THE NUMBER3: "))
if num1>num2 and num1>num3:
    print(f"{num1} IS LARGEST")
elif num2>num1 and num2>num3:
    print(f"{num2} IS LARGEST")
elif num3>num1 and num3>num2:
    print(f"{num3} IS LARGEST")
else:
    print("NUMBERS ARE EQUAL")
    


