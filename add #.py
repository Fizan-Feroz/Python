fname="fiz.txt"
f=open(fname,'r')
items=[]
for a in f:
    words=a.split()
    for x in words:
        items.append(x)
print("#".join(items))
