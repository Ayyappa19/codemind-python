n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    k.append(i*i)

print(*(sorted(k)))
    