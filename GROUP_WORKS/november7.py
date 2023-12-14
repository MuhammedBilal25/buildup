# 1.Write a program to accept two numbers and mathematical operators and perform operation accordingly
# Output: Enter 1st number :10
# Enter 2nd number:5
# Enter operator: -
# The answer:5
# n1=int(input("Enter 1st number :"))
# n2=int(input("Enter 2nd number:"))
# op=input("Enter operator:")
# if op=="+":
#     res=n1+n2
#     print(f"The answer:{res}")
# elif op=="-":
#     res=n1-n2
#     print(f"The answer:{res}")
# elif op=="*":
#     res=n1*n2
#     print(f"The answer:{res}")
# elif op=="/":
#     res=n1/n2
#     print(f"The answer:{res}")
# elif op=="%":
#     res=n1%n2
#     print(f"The answer:{res}")
# elif op=="//":
#     res=n1//n2
#     print(f"The answer:{res}")
# else:
#     print(f"{op} is invalid operator")
# 2. Take input of age of 3 people by user and determine oldest and youngest among them.
# a1=int(input("Enter 1st person age:"))
# a2=int(input("Enter 2nd person age:"))
# a3=int(input("Enter 3rd person age:"))
# if a1==a2==a3:
#     print(f"all are equal")
# elif a1>=a2>=a3:
#     print(f"{a1} is oldest and {a3} is youngest")
# elif a2>=a1>=a3:
#     print(f"{a2} is oldest and {a3} is youngest")
# elif a3>=a2>=a1:
#     print(f"{a3} is oldest and {a1} is youngest")
# elif a1>=a3>=a2:
#     print(f"{a1} is oldest and {a2} is youngest")
# elif a2>=a3>=a1:
#     print(f"{a2} is oldest and {a1} is youngest")
# elif a3>=a1>=a2:
#     print(f"{a3} is oldest and {a2} is youngest")
# 3. Take values of length and breadth of a rectangle from user and check if it is square or not.
length=int(input("ENTER THE LENGTH:"))
bredth=int(input("ENTER THE BREDTH:"))
if length==bredth:
    print("SQUARE")
else:
    print("RECTANGLE")

