def add(*args):
    return sum(args)
print(add(10,40,70,80))
def product(*args):
    r=1
    for i in args:
        r=r*i
    return r
def lsum(*args):
    d=[i%10 for i in args]
    return sum(d)
def last_digit_max(*args):
    return max([i%10 for i in args])
print(last_digit_max(123,134,135,18,19))

    
