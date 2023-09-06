s=input()
k="aeiou"
l="AEIOU"
c=0
cn=0
q=""
for i in s:
    if i in k:
        if i not in q:
            c+=1
            q+=i
    elif i in l:
        if i not in q:
            cn+=1
            q+=i
if(c==5 or cn==5):
    print(True)
else:
    print(False)
            