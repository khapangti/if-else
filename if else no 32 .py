units=int(input("enter number of units"))
if units>=100 and units<200:
    price=units*5
    print("electricity bill",price)
elif units>=200:
    price=units*10
    print("electricity bill",price)
else:
    print("no charge")