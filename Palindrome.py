n=int(input())
p=0
a=n
while(n):
    r=n%10
    p=p*10+r
    n=n//10
if(p==a):
    print('True')
else:
    print('False')