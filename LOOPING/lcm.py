# LCM
n1=int(input("ENTER THE FIRST NUMBER = "))
n2=int(input("ENTER THE SECOND NUMBER = "))
greatest= n1 if n1>n2 else n2
product=n1*n2
while greatest<=product:
    if greatest%n1==0 and greatest%n2==0:
        lcm=greatest
        break
    greatest+=1
print(lcm)