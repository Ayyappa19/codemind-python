st=input()
s=st.split(" ")
sr=''
for i in range(len(s)):
    if( i%2==0):
       k= s[i][::-1]
       sr+=k
       sr+=" "
    else:
        sr+=s[i]
        sr+=" "
    
print(sr[:len(st):])
