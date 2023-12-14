pre=0
cur=1
print(f"{pre},{cur}",end=",")
for i in range(1,11):
    next=pre+cur
    print(next,end=",")
    pre=cur
    cur=next