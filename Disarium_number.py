n=input()
l=len(n)
k=1
s=0
for i in n:
    for j in range(k,l+1):
        f=(int(i))**k
        k+=1
        break
    s=s+f
# print(s)
if(int(n)==s):
    print('True')
else:
    print('False')