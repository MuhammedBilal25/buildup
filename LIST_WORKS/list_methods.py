orders=["friedrice","ghrrroast","vb","cb","bb","bb","vb","cb","vb","cb"]
orders.append("tea")
items=["chai","kappi"]
print(orders)
print(orders.count("bb"))
print(orders.index("vb"))
print(orders.pop())
hack=orders.copy()#this is not same as hack=orders->(chainging hack wil change orders) if we use copy only one wil change
print(hack) 
orders.insert(5,"mb")
print(orders)
orders.extend(items)
print(orders)
orders.remove("kappi")
print(orders)
orders.reverse()
print(orders)
orders.sort()
print(orders)
