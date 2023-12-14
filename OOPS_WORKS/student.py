class Student:
    name:str
    rollno:int
    def set_student(self,name,rno):
        self.name=name
        self.rollno=rno
    def display(self):
        print(self.rollno,self.name)
st1=Student()
st1.set_student("Bilal",2)
st1.display()
st2=Student()
st2.set_student("Manoj",9)
st2.display()
