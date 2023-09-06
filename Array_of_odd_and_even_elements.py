n=int(input())
l=list(map(int,input().split()))
k=[]
q=[]
for i in l:
    if(i%2==0):
        k.append(i)
    if(i%2==1):
        q.append(i)
f=q+k
print(*f)