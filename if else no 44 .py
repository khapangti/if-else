a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if a>b and a<c or a>c and a<b:
    print("a is second largest number")
elif b>a and b<c or b>c and b<a:
    print("b is second largest number")
elif c>a and c<b or c>b and c<a:
    print("c is second largest number")
else:
    print("same")