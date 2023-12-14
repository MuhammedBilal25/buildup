year=int(input("ENTER THE YEAR :" ))
if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
    print(f"{year} IS LEAP YEAR")
else:
    print( f"{year} IS NOT A LEAP YEAR")
