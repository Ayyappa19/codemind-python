n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
ans = 0
for ii in range(n):
    if(l[ii]>=a and l[ii]<=b):
        continue
    else:
        k.append(l[ii])
c=len(k)
if(c>0):
    print(*k)
else:
    print(-1)

    
