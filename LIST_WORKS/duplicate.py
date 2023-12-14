# arr=[4,9,5,6,9,5,4]
# arr.sort()
# count=1
# i=0
# while i<len(arr)-1:
#     j=i+1
#     ith_element=arr[i]
#     jth_element=arr[j]
#     difference=jth_element-ith_element
#     if difference==0:
#         print(ith_element)
#         i=j
#     i+=1
arr=[4,9,5,6,9,7,4]
count=0
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i]==arr[j]):
            print(arr[j])
        count+=1
print(count)
