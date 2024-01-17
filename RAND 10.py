import random
l=[]
for i in range(10):
    x=random.randint(10,99)
    l.append(x)
print("og list",l)
l1=l[5:]
l2=l[:5]
print("firstb 5 ele:",l1)
print("last 5 ele:",l2)