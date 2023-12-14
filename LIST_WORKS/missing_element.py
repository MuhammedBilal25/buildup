arr=[1,4,2,6,8,9,11]
arr.sort()
i=0
while(i<len(arr)-1):
    j=i+1
    ith_element=arr[i]
    jth_element=arr[j]
    diff=jth_element-ith_element
    if diff!=1:
        print(ith_element+1)
    i+=1
