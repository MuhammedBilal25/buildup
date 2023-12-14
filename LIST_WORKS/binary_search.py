lst=[10,12,4,8,2,9]
lst.sort()
element=int(input("ENTER THE ELEMENT : "))
lower=0
upper=len(lst)-1
is_present=False
while lower<=upper:
    mid=(lower+upper)//2
    if element==lst[mid]:
        is_present=True
        break
    elif element<lst[mid]:
        upper=mid-1
    elif element>lst[mid]:
        lower=mid+1
print(is_present)