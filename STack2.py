l=[]
y="y"
while y=="y":
    print("1.PUSH")
    print("2.POP")
    print("3.DISPLAY")
    c=int(input("ENTER CJOICE"))
    if c==1:
        x=int(input("Enter a number:"))
        l.append(x)
    if c==2:
        if l==[]:
            print("stack empty")
        else:
            print("Deleted elememnt is:",l.pop())
    if c==3:
        x=len(l)
        for i in range(x-1,-1,-1):
            print(l[i])
