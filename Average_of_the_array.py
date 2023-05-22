n=int(input())
l=list(map(int,input().split()))
#k=int(input())
x=len(l)
s=0
for i in range(x):
    s=s+l[i]
av=s/x
# c=0
# for i in range(x):
#     if(av==l[i]):
#         c+=1
#         break
# if(c==1):
#     print('True')
# else:
#     print('False')
print(f'{av:.2f}')