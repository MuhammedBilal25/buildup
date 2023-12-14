class Book:
    name:str
    author:str
    pages:int
    price:int
    def __init__(self,name,author,pg,price):#constructor, it invokes when object is initialised
        self.name=name
        self.author=author
        self.pages=pg
        self.price=price
    def display(self):
        print(self.name,self.author)
    def __str__(self):
        return self.name
b1=Book("Randamoozham","mt",476,700)
b1.display()
print(b1)