grid=[
 [0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
direct={}
def dfs(row,col):
    tmp_dir={}
    tmp_stack=[]
    tmp_stack.append((row,col))
    while len(tmp_stack):
        tmp_node=tmp_stack[len(tmp_stack)-1]
        tmp_dir[tmp_node]=1
        direct[tmp_node]=1
        for r,c in ((-1,0),(1,0),(0,1),(0,-1)):
            flag=0
            if 0<=tmp_node[0]+r<len(grid) and 0<=tmp_node[1]+c<len(grid[0]) and grid[tmp_node[0]+r][tmp_node[1]+c]==1 and not tmp_dir.get((tmp_node[0]+r,tmp_node[1]+c)):
                tmp_stack.append((tmp_node[0]+r,tmp_node[1]+c))
                flag=1
                break
        if flag==0:tmp_stack.pop()
    return len(tmp_dir)
max_area=0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]==1 and not direct.get((i,j)):max_area=max(max_area,dfs(i,j))
print(max_area)



