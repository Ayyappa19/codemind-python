n=int(input())
l=list(map(int,input().split()))
# a=int(input())
s=0
for i in l:
    if(i%2==1):
        break
    else:
        s+=i
print(s)

