num=int(input("enter first number"))
num2=int(input("enter second number"))
operator=input("enter number")
if operator=="+":
    print(num+num2)
elif operator=="-":
    print(num-num2)
elif operator=="*":
    print(num*num2)
elif operator=="/":
    print(num/num2)
elif operator=="%":
    print(num%num2)
elif operator=="**":
    print(num**num2)
elif operator=="//":
    print(num//num2)
else:
    print("same")