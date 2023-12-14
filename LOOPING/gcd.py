# HCF
n1=int(input("ENTER THE FIRST NUMBER = "))
n2=int(input("ENTER THE SECOND NUMBER = "))
smallest_num=n1 if n1<n2 else n2
i=1
while i<=smallest_num:
    if n1%i==0 and n2%i==0:
        fact=i
    i+=1
print(f"GCD OF {n1} AND {n2} IS {fact}")