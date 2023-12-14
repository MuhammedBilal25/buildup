class Employee:
    id:int
    name:str
    department:str
    salary:int
    def set_emp(self,id,name,dp,sal):
        self.id=id
        self.name=name
        self.department=dp
        self.salary=sal
    def display(self):
        print(self.id,self.name,self.department,self.salary)
emp1=Employee()
emp1.set_emp(1,"vijay","Thalapathy",130000000)
emp1.display()
emp2=Employee()
emp2.set_emp(2,"mammuka","Megastar",70000000)
emp2.display()
emp3=Employee()
emp3.set_emp(3,"SRK","King-Khan",1000000000)
emp3.display()
emp4=Employee()
emp4.set_emp(4,"surya","naippin-mannan",130000000)
emp4.display()

