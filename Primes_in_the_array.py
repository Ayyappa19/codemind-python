def prime(n):
    if n==1:
        return False
    c=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            c+=1
            break
    return c==0
n=int(input())
l=list(map(int,input().split()))

c=0
for i in l:
    if prime(i):
        c+=1
print(c)