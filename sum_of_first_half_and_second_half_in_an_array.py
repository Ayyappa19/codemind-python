n=int(input())
l=list(map(int,input().split()))
# a=int(input())
k=n//2
l1=l[:k:]
l2=l[k::]
a=sum(l1)
b=sum(l2)
print(a)
print(b)
