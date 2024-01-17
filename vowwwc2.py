def isvow(char):
    vowels="AEIOUaeiou"
    return char in vowels
def iscon(char):
    return char.isalpha() and not isvow(char)
vc=0
cc=0
uc=0
lc=0
fname="fiz.txt"
with open(fname,'r')as f:
    d=f.read()
    for char in d:
        if isvow(char):
            vc+=1
        if iscon(char):
            cc+=1
        if char.islower():
            lc+=1
        if char.isupper():
            uc+=1
    print("Vowels",vc)
    print("consonants",cc)
    print("low",vc)
    print("upper",uc)
    vvv=00