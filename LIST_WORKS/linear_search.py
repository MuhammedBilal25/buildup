lst=[10,2,11,5,7,20]
element=int(input("enter the element : "))
is_found=False
for i in range(0,len(lst)):
    cur_elelment=lst[i]
    if cur_elelment==element:
        is_found=True
        break
print(is_found)