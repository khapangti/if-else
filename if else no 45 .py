days=int(input("enter number"))
if days<=5:
    amount=days*2
    print("library charge:",amount)
elif days>=6 and days<10:
    amount=days*3
    print("library charge:",amount)
elif days>=10 and days<=15:
    amount=days*4
    print("library charge:",amount)
elif days>15:
    print("library charge:",amount)
else:
    print("none")