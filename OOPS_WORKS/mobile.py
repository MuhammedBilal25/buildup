class Mobile:
    name:str
    brand:str
    price:int
    def __init__(self,name,brand,price):
        self.name=name
        self.brand=brand
        self.price=price
    def display(self):
        print(f"{self.name} is launched by {self.brand} at the price of Rs{self.price}")
    def __str__(self):
        return self.name
m1=Mobile("s23","samsung",123000)
m1.display()
print(m1)