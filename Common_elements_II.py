a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
v=[]
for i in l1:
    if i not in l2:
        v.append(i)
for j in l2:
    if j not in l1:
        v.append(j)
for x in v:
    print(x,end=" ")