n=int(input())
l=list(map(int,input().split()))
for i in l:
    c=l.count(i)
    if(c>n//2):
        print(i)
        break