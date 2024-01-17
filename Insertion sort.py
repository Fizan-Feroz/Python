og=[88,10,23,47,55,12]
print("Original list:",og)
for i in og:
    j=og.index(i)
    while j>0:
        if og[j-1]>og[j]:
            og[j-1],og[j]=og[j],og[j-1]
        else:
            break
        j=j-1
print(og)