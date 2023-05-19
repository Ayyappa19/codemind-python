n=int(input())
if(n<0):
    p=-1*n
    re=0
    while(p!=0):
        r=p%10
        re=re*10+r
        p=p//10
    print(-1*re)
else:
    rev=0
    while(n!=0):
        b=n%10
        rev=rev*10+b
        n=n//10
    print(rev)
    
    