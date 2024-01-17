file1='fizan1.txt'
file2='fizan2.txt'
f1=open(file1,'r')
f2=open(file2,'w')
for i in f1:
    if "a" not in i:
        f2.write(i)
f1.close()
f2.close()