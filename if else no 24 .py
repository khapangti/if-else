a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if a>b and a>c:
    print("a is oldest")
elif b>a and b>c:
    print("b is oldest")
elif c>a and c>b:
    print("c is oldest")
if a<b and a<c:
    print("a is youngest")
elif b<a and b<c:
    print("b is youngest")
elif c<a and c<b:
    print("c is youngest")
else:
    print("none")