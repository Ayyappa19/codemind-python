s1=input()
s=s1.lower()

k='abcdefghijklmnopqrstuvwxyz1234567890 '
c=0
for i in s:
    if i not in k:
        c+=1
print(c)
    