print("LEAP YEAR BETWEEN 1800 T0 2024 ARE")
for year in range(1800,2025):
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        print(year)