def leap_year(year):
    res=True if year%100==0 and year%400==0 or year%100!=0 and year%4==0 else False
    return res
print(leap_year(2016))
