n=int(input())
l=list(map(int,input().split()))
l.reverse()
for i in range(len(l)):
    if(l[i]%2!=0):
        k=n-i-1
        print(k)
        break
        