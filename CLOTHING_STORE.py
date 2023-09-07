from collections import Counter
n=int(input())
l=list(map(int,input().split()))
n = Counter(l)
print(sum(i//2 for i in n.values()))
    