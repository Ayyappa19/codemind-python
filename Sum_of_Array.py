n=int(input())
l=list(map(int,input().split()))
x=len(l)
s=0
for i in range(x):
    # if(i%2!=0):
    s=s+l[i]
print(s)