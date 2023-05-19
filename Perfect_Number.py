n=int(input())
sum=0
p=n
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum==p):
    print('True')
else:
    print('False')
        