def isvow(char):
    vowels='AEIOUaeiou'
    return char in vowels
def iscons(char):
    return char.isalpha() and not isvow(char)
vc=0
cc=0
uc=0
lc=0
with open('fiz.txt','r') as f:
    d=f.read()
    for char in d:
        if char.isupper():
            uc+=1
        if char.islower():
            lc+=1
        if isvow(char):
            vc+=1
        if iscons(char):
            cc+=1
print("Consonants",cc)
print("vow",vc)
print("upper",uc)
print("lowwer",lc)