# 1.Write a python program to convert the temperature in degree centigrade to fahrenheit
temp_d_cel=int(input("enter the temperature in degree centigrade:"))
temp_in_F=(temp_d_cel*9/5)+32
print(f"{temp_d_cel}degree celcius is equal to {temp_in_F}F")
# 2. Write a python program to find compound interest
p=int(input("enter the amount to invest:"))
rate_of_interest=0.05
number_of_times_interest_get_copounter_per_yesr=1
n=int(input("NUMBER OF PERIOD MONEY INVESTED FOR:"))
temp=p
for i in range(0,n):
    temp=temp*((1+rate_of_interest/n)**(n*number_of_times_interest_get_copounter_per_yesr))
ci=temp-p
print(ci)
# 3. Write a python program to find area of a circle.
r=int(input("ENTER THE RADIUS:"))
area=3.14*r*r
print(area)
