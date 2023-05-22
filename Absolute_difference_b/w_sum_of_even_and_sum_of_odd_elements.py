n=int(input())
l=list(map(int,input().split()))
x=len(l)
se=0
so=0
for i in range(x):
    if(l[i]%2==0):
        se=se+l[i]
    else:
        so=so+l[i]
print(int(((se-so)**2)**0.5))