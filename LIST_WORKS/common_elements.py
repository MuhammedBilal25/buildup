lst1=[9,4,3,10,15]
lst2=[5,4,2,3,20]
# for i in range(0,len(lst1)):
#     for j in range(0,len(lst2)):
#         if lst1[i]==lst2[j]:
#             print(lst1[i])
lst1.sort()
lst2.sort()
p1=0
p2=0
while(p1<len(lst1) and p2<len(lst2)):
    if lst1[p1]==lst2[p2]:
        print(lst1[p1])
        p1+=1
        p2+=1
    elif lst1[p1]>lst2[p2]:
        p2+=1
    elif lst1[p1]<lst2[p2]:
        p1+=1
    




