s=input()
k="aeiou"
q=''
c=0
for i in s:
    if i in k:
        if i not in q:
            c+=1
            q+=i
if(c==5):
    print(0)
else:
    for i in k:
        if i not in q:
            print(i,end=" ")

        