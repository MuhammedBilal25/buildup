fr=open("C:\\Users\\USER\\Desktop\\L-P\\FILE_INPUT_OUTPUT\\years.txt","r")
fw=open("C:\\Users\\USER\\Desktop\\L-P\\FILE_INPUT_OUTPUT\\leap_years.txt","w")
for line in fr:
    year=int(line.rstrip("\n"))
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        fw.write(str(year)+"\n")
    

