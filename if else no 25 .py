a=int(input("enter number of classes held"))
b=int(input("enter number of classes attended"))
percent=b*100/a
if percent<75:
    print("the student is not allowed to sit in the exam=",percent)
else:
    print("the student is allowed to sit in the exam=",percent)