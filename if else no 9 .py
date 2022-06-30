ch=input("enter number")
if ch>="a" and ch<="z" or ch>="A" and ch<="Z":
    print("it is an alphabet")
elif ch>="0" and ch<="9":
    print("it is digit")
else:
    print("special character")