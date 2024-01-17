s=[]
y="y"
while y == "y":
    print("1.push")
    print("2 pop")
    print("3 display")
    c= int(input("Enter selection"))
    if c==1:
        x=int(input("enter a number"))
        s.append(x)
    elif c==2:
        if s==[]:
            print("stack empty")
        else:
            print("the deleted element is:",s.pop())
    elif c==3:
        l=len(s)
        for i in range(l-1,-1,-1):
            print(s[i])
    y=input("Do you want to continue?(y/n)")
