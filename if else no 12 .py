month=input("enter month")
a=("january","march","may","july","august","october","december")
b=("april","june","september","november")
if month in (a):
    print("31 days in", month)
elif month in (b):
    print("30 days in", month)
else:
    print("28 days in", month)