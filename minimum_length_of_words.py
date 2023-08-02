s=input()
t=s.split()
c=len(s)
for i in t:
    if(len(i)<=c):
        c=len(i)
print(c)