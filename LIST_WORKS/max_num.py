lst=[23,12,78,9]
#ans =9782312
str_num=[str(n) for n in lst]
str_num.sort(reverse=True)
llst=[int(n) for n in str_num]
for n in lst:
    print(n,end="")