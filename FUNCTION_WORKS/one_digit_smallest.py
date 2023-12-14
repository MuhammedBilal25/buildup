def one_digit_smallest(n1,n2):
    ns1=n1%10
    ns2=n2%10
    res=n1 if ns1<ns2 else n2
    return res
print(one_digit_smallest(432,18))
