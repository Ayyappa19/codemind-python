n=int(input())
l=list(map(int,input().split()))
k=int(input())
x=len(l)
s=0
for i in range(x):
    if(k==l[i]):
        s+=1
        break
if(s==1):
    print('True')
else:
    print('False')