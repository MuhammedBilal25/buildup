students=open("C:\\Users\\USER\\Desktop\\L-P\\FILE_INPUT_OUTPUT\\students.txt","r")
failed=open("C:\\Users\\USER\\Desktop\\L-P\\FILE_INPUT_OUTPUT\\failed.txt","r")
students_set={line.rstrip("\n") for line in students}#set comprehension
failed_set=set()
for line in failed:
    st=line.rstrip("\n")
    failed_set.add(st)
passed=students_set.difference(failed_set)
print(passed)