phy=int(input("enter marks "))
ch=int(input("enter marks"))
bio=int(input("enter number"))
math=int(input("enter number"))
comp=int(input("enter marks"))
total=phy+ch+bio+math+comp
percent=total*100/500
if percent>=90:
    print("grade A",percent)
elif percent>=80:
    print("grade B",percent)
elif percent>=70:
    print("grade C",percent)
elif percent>=60:
    print("grade D",percent)  
elif percent>=40:
    print("grade E",percent)  
else:
    print("grade F",percent)