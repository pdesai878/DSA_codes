from collections import deque
def dfs(i,j):
    grid[i][j]='#'
    for dir in range(4):
        x=i+row[dir]
        y=j+col[dir]
        if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]=='1':
            dfs(x,y)

def bfs(i,j):
    q=deque()
    q.append([i,j])
    grid[i][j]='0'

    while q:
        i,j=q.popleft()
        for x,y in [[i-1,j],[i,j+1],[i+1,j],[i,j-1]]:
            if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]=='1':
                q.append([x,y])
                grid[x][y]=0 

 
grid=[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]               
row=[-1,0,1,0]
col=[0,1,0,-1]
count=0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]=='1':
            bfs(i,j)
            count+=1
    

print(count)