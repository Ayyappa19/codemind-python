n=int(input())
ls=len(str(n))
lss=len(set(str(n)))
if(ls==lss):
    print('Unique Number')
else:
    print('Not Unique Number')