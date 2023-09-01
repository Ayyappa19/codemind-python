n=int(input())
l=list(map(int,input().split()))
m,c=0,0
ans = 0
if(n==1  or n==0):
    print(0)
else:
    for i in range(0, n):
        if(l[i]%2==0):
            c+=1
            if(c > 2):
                ans +=1
        else:
            c=0
    print(ans)
    
