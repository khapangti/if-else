age=int(input("enter age"))
sex=input("enter gender")
nd=int(input("enter number"))
if age>=18 and age<30 and sex=="M":
    amount=nd*700
    print("total wage is=",amount)
elif age>=18 and age<30 and sex=="F":
    amount=nd*750
    print("total wage is=",amount)
elif age>=30 and age<=40 and sex=="M":
    amount=nd*800
    print("total wage is=",amount)
elif age>=30 and age<=40 and sex=="F":
    amount=nd*850
    print("total wage is",amount)
else:
    print("same")