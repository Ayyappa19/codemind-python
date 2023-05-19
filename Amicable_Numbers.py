def amnum(n):
    su=0
    for i in range(1,n):
        if(n%i==0):
            su=su+i
    return su
n=int(input())
m=int(input())
nn=amnum(n)
mm=amnum(m)
if(nn==m and mm==n):
    print('Amicable')
else:
    print('Not Amicable')