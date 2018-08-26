import copy
#二维列表的深拷贝
matrix=[[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
# res=[[float('inf')]*len(matrix[0])for _ in range(len(matrix))]
# note=[]
# for row,i in enumerate(matrix):
#     for col,j in enumerate(i):
#         if j==0:res[row][col]=0
#         else:note.append((row,col))
# tmp_res=[]
# while tmp_res!=res:
#     tmp_res=res[:][:]
#     for i,j in note:
#         for row,col in [(-1,0),(1,0),(0,-1),(0,1)]:
#             if 0<=i+row<len(matrix) and 0<=j+col<len(matrix[0]):
#                 res[i][j]=min(res[i+row][j+col]+1,res[i][j])
# print(res)
#两次遍历，先左上，后右下
res=[[float('inf')]*len(matrix[0])for _ in range(len(matrix))]
for row,i in enumerate(matrix):
    for col,j in enumerate(i):
        if j==0:res[row][col]=0
        else: 
            if row>0:
                res[row][col]=min(res[row][col],res[row-1][col]+1)
            if col>0:
                res[row][col]=min(res[row][col],res[row][col-1]+1)
for row in range(len(matrix)-1,-1,-1):
    for col in range(len(matrix[0])-1,-1,-1):
        if res[row][col]!=0:
            if row<len(matrix)-1:
                res[row][col]=min(res[row][col],res[row+1][col]+1)
            if col<len(matrix[0])-1:
                res[row][col]=min(res[row][col],res[row][col+1]+1)
print(res)