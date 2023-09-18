n=int(input())
l=list(map(int,input().split()))
a=int(input())
k=l.index(a)
l1=l[:k+1:]
print(sum(l1))

