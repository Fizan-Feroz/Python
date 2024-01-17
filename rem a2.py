file1=open("fizan1.txt",'r')
file2=open("fizan2.txt",'w')
for l in file1:
    if "a" not in l:
        
        file2.write(l)
file1.close()
file2.close()
print("Removed all lines with 'a'")