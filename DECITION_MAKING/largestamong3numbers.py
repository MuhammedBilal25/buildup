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
    