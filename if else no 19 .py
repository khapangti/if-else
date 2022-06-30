basic_salary=int(input("enter number"))
if basic_salary<=10000:
    hra=basic_salary/100*20
    da=basic_salary/100*80
    gross_salary=basic_salary+hra+da
    print("gross salary",gross_salary)
elif basic_salary<=20000:
    hra=basic_salary/100*25
    da=basic_salary/100*90
    gross_salary=basic_salary+hra+da
    print("gross salary",gross_salary)
elif basic_salary>20000:
    hra=basic_salary/100*30
    da=basic_salary/100*95
    gross_salary=basic_salary+hra+da
    print("gross salary",gross_salary)
else:
    print("none")