amount=int(input("enter amount"))
if amount>=5:
    a=amount//2000
    b=amount%2000
    c=b//500
    d=b%500
    e=d//200
    f=d%200
    g=f//100
    h=f%100
    i=h//50
    j=h%50
    k=j//20
    l=j%20
    m=l//10
    n=l%10
    o=n//5
    print("note of 2000=",a,"note of 500=",c,"note of 200=",e,"note of 100=",g,"note of 50=",i,"note of 20=",k,"note of 10=",m,"note of 5=",o)
else:
    print("not available")