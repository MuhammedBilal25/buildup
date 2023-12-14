cube=lambda n:n**3
print(cube(3))

num_check=lambda n:"POSITIVE" if n>0 else "NEGATIVE" if n<0 else "ZERO"
print(num_check(-4))

max_two=lambda n1,n2:n1 if n1>n2 else n2 
print(max_two(2,5))
odd_even=lambda n:"even" if n%2==0 else "odd"
print(odd_even(6))