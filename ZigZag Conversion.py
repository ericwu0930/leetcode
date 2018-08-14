s = "AB"
numRows=1
curRow=0
direction=0 #0朝下
res={}
for i in s:
    res.setdefault(curRow,[]).append(i)
    if direction==0 and curRow+1<numRows:
        curRow+=1
    elif direction==1 and curRow-1>=0:
        curRow-=1
    elif direction==0 and curRow+1>=numRows:
        direction=1
        curRow-=1
    elif direction==1 and curRow-1<0:
        direction=0
        curRow+=1
for i in res.values():
    print (''.join(i),end='')





