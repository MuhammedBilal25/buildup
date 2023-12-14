f=open("C:\\Users\\USER\\Desktop\\L-P\\FILE_INPUT_OUTPUT\\century_year.txt","w")
for i in range(1800,2024):
    if i%100==0:
        f.write(str(i)+"\n")

