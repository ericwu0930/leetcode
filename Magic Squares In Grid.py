# 河图中心数字必为5，各行各列各斜边之和必为15
grid=[[1,8,6],[10,5,0],[4,2,9]]
def magic_grid(i,j):
    if grid[1+j][1+i]!=5:return False
    for row in range(3):
        sum=0
        for col in range(3):
            if grid[row+j][col+i]>=10:return False
            sum+=grid[row+j][col+i]
        if sum!=15:return False
    for col in range(3):
        sum=0
        for row in range(3):
            sum+=grid[row+j][col+i]
        if sum!=15:return False
    if grid[j][i]+grid[1+j][1+i]+grid[2+j][2+i]!=15 or grid[2+j][i]+grid[1+j][1+i]+grid[j][2+i]!=15:
        return False
    else:return True
sum=0
for i in range(len(grid[0])-2):
    for j in range(len(grid)-2):
        if magic_grid(i,j):sum+=1
print(sum)
