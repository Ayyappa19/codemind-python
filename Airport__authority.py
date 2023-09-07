n=int(input())
s=0
l=[]
for i in range(n):
    k=int(input())
    l.append(k)
f=int(input())
for i in l:
    if(i<=f):
        s+=1
    else:
        s+=2
print(s)
    