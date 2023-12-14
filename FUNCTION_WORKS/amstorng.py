def armstrong(num):
    digit_count=len(num)
    num=int(num)
    temp=num
    sum=0
    while (num!=0):
        digit=num%10
        exp=digit**digit_count
        sum=sum+exp
        num=num//10
    if sum==temp:
        return True
    else:
        return False
    

    
print(armstrong("153"))