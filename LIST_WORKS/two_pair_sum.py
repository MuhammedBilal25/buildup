list=[3,4,5,2,6]
sum=int(input("ENTER THE SUM : "))
list.sort()
# for i in range(0,len(list)-1):
#     for j in range(i+1,len(list)):
#         cur_sum=list[i]+list[j]
#         if sum==cur_sum:
#             print(f"pair is {list[i]} {list[j]}")
#             break
lower=0
upper=len(list)-1
while(lower<upper):
    current_sum=list[lower]+list[upper]
    if current_sum==sum:
        print(f"pairs are {list[lower]},{list[upper]}")
        lower+=1
        upper-=1
    elif current_sum<sum:
        lower+=1
    elif current_sum>sum:
        upper-=1
    



