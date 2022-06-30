quantity=int(input("enter quantity"))
total_cost=quantity*100
if total_cost>1000:
    unit=total_cost*10/100
    cost=total_cost-unit
    print("total_cost of units",cost)
else:
    print("only total_cost",total_cost)