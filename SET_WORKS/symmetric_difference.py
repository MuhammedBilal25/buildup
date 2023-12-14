# symmetric difference
order1={"cb","tika","fishfry","friedrice","vb","gheerost"}
order2={"cb","friedrice","nan","upuma","vegmeals","idly"}
# common_orders=order1.intersection(order2)
# orders=order1.union(order2)
# final_orders=orders.difference(common_orders)
final_orders=order1.symmetric_difference(order2)
print(final_orders)