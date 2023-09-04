s=input()
k=s.lower()
l=k.split(" ")
c=0

for i in l:
    f=i[::-1]
    if(i==f):
        c+=1
print(c)
    