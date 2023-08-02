s=input()
t=s.split()
c=len(s)
for i in t:
    if(c>=len(i)):
        c=len(i)
print(c)