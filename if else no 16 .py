a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if a==b==c:
    print("equilateral triangle")
elif a==b or b==c or c==a:
    print("isosceles triangle")
else:
    print("scalene trianlge")