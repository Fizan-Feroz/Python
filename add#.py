f=open('fiz.txt','r')
item=[]
for l in f:
    w=l.split()
    for i in w:
        item.append(i)
        print("h")
print("#".join(item))