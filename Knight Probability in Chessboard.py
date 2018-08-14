N=1
K=1
r=0
c=0
def inBoard(r,c,times):
    if times!=0:
        times-=1
        position=[(r-2,c-1),(r-2,c+1),(r+2,c-1),(r+2,c+1),(r-1,c-2),(r-1,c+2),(r+1,c-2),(r+1,c+2)]
        for i in position:
            if i[0]<0 or i[0]>=N or i[1]<0 or i[1]>=N:
                continue
            else:
                inBoard(i[0],i[1],times)
    else:
        result[0]+=1
result=[0]
inBoard(r,c,K)
print(result[0]/8**K)

