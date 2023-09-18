n=int(input())
l=list(map(int,input().split()))
# a=int(input())
k=n//2
l1=l[:k:]
l2=l[k::]
b=sum(l1)-sum(l2)
if(b<0):
    print(-1*b)
else:
    print(b)
