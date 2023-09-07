import math
n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    k=int(math.sqrt(i))
    if(k*k==i):
        s+=i
print(s)