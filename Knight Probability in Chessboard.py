N=3
K=2
r=0
c=0
# def inBoard(r,c,times):
#     if times!=0:
#         times-=1
#         position=[(r-2,c-1),(r-2,c+1),(r+2,c-1),(r+2,c+1),(r-1,c-2),(r-1,c+2),(r+1,c-2),(r+1,c+2)]
#         for i in position:
#             if i[0]<0 or i[0]>=N or i[1]<0 or i[1]>=N:
#                 continue
#             else:
#                 inBoard(i[0],i[1],times)
#     else:
#         result[0]+=1
# result=[0]
# inBoard(r,c,K)
# print(result[0]/8**K)

dp=[[0]*N for _ in range(N)]
dp[r][c]=1
for i in range(K):
    dp2=[[0]*N for _ in range(N)]
    for row,m in enumerate(dp):
        for col,n in enumerate(m):
            if n!=0:
                for dr,dc in ((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)):
                    if 0<=row+dr<N and 0<=col+dc<N:
                        dp2[row+dr][col+dc]+=n
    dp=dp2
print(sum(map(sum,dp))/8**K)
                    