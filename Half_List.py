n=int(input())
l=list(map(int,input().split()))
k=n//2
g=l[k::]
e=g[::-1]
f=l[:k:]
l1=e+f
print(*l1)