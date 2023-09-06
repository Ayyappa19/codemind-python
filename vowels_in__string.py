s=input()
k="aeiouAEIOU"
c=0
q=""
for i in s:
    if i in k:
        if i not in q:
            c+=1
            q+=i+" "
            
f=q[:len(q)-1:]        
if(c==0):
    print(-1)
else:
    print(f)