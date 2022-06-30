cost_price=int(input("enter price"))
if cost_price>100000:
    price=cost_price*15/100
    print("tax=",price)
elif cost_price>50000 and cost_price<=100000:
    price=cost_price*10/100
    print("tax=",price)
elif cost_price<=50000:
    price=cost_price*5/100
    print("tax=",price)
else:
    print("no tax")