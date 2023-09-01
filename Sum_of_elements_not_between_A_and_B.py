n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
ans = 0
for ii in range(n):
    if(l[ii]>=a and l[ii]<=b):
        continue
    else:
        s+=l[ii]
print(s)
    
