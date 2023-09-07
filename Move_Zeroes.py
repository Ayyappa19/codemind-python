n=int(input())
l=list(map(int,input().split()))
k=[]
f=[]
for i in l:
    
    if(i==0):
        # f=l.remove(0)
        k.append(0)
    else:
        f.append(i)
l1=f+k
print(*l1)