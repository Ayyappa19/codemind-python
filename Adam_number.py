def rev(n):
    p=0
    while(n):
        r=n%10
        p=p*10+r
        n=n//10
    return p
    
n=int(input())
a=rev(n)
x=n*n
y=a*a
if(x==rev(y)):
    print('True')
else:
    print('False')

