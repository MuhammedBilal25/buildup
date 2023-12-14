f=open("C:\\Users\\USER\\Desktop\\L-P\\FILE_INPUT_OUTPUT\\years.txt","r")
for line in f:
    year=int(line.rstrip("\n"))
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        print(year)
    

