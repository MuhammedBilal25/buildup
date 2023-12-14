num1=int(input("ENTER THE NUMBER1: "))
num2=int(input("ENTER THE NUMBER2: "))
num3=int(input("ENTER THE NUMBER3: "))
if num1>num2 and num1>num3:
    print(f"{num1} is largest")
    if num2>num3:
        print(f"{num2} IS 2nd LARGEST")
        print(f"{num3} IS SMALLEST")
    else:
         print(f"{num3} IS 2nd LARGEST")
         print(f"{num2} IS SMALLEST")
elif num2>num1 and num2>num3:
    print(f"{num2} is largest")
    if num1>num3:
        print(f"{num1} IS 2nd LARGEST")
        print(f"{num3} IS SMALLEST")
    else:
        print(f"{num3} IS 2nd LARGEST")
        print(f"{num1} IS SMALLEST")
elif num3>num1 and num3>num2:
    print(f"{num3} is largest")
    if num1>num2:
        print(f"{num1} IS 2nd LARGEST")
        print(f"{num2} IS SMALLEST")
    else:
         print(f"{num2} IS 2nd LARGEST")
         print(f"{num1} IS SMALLEST")
elif num1==num2 and num1==num3:
    print("NUMBERS ARE EQUAL")
    