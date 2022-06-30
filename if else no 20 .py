units=int(input("enter number"))
if units<=50:
    amount=units*0.50
    surcharge=amount*20/100
    total=amount+surcharge
    print("electricity bill=",total)
elif units<=100:
    amount=units*0.75
    surcharge=amount*20/100
    total=amount+surcharge
    print("electricity bill=",total)
elif units<=100:
    amount=units*1.20
    surcharge=amount*20/100
    total=amount+surcharge
    print("electricity bill=",total)
elif units>=250:
    amount=units*1.50
    surcharge=amount*20/100
    total=amount+surcharge
    print("electricity bill=",total)
else:
    print("none")