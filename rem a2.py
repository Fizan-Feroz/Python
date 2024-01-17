file1=open("fizan1.txt",'r')
file2=open("fizan2.txt",'w')
for l in file1:
    if "a" not in l:
        print("a")
        file2.write(l)