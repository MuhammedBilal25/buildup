selling_price=int(input("enter the selling price"))
cost_price=int(input("enter the cost price"))
profit=selling_price-cost_price
print(f"profit={profit}")
profit_perc=(profit/cost_price)*100
print(f"profit%={profit_perc}") 
print(f"a product whose cost price is {cost_price} sold for {selling_price} and made a profit of {profit_perc}%")
