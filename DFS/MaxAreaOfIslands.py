class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            grid[i][j]=0
            s=1
            for x,y in [[i-1,j],[i,j+1],[i+1,j],[i,j-1]]:
                if 0<=x<row and 0<=y<col and grid[x][y]==1:
                    s+=dfs(x,y)
            return s
                    
        row=len(grid)
        col=len(grid[0])
        mx=0
        for i in range(row):
            for j in range(col): 
                if grid[i][j]==1:                  
                    mx=max(mx,dfs(i,j))
        return mx

# def dfs(i,j):
#     grid[i][j]=0
#     self.area+=1      #this can also be done!  
#     for x,y in [[i-1,j],[i,j+1],[i+1,j],[i,j-1]]:
#         if 0<=x<row and 0<=y<col and grid[x][y]==1:
#             dfs(x,y)



# def bfs(i,j):
#     q=deque()
#     q.append([i,j])
#     grid[i][j]=0

#     count=0
#     while q:
#         a,b=q.popleft()
#         count+=1
#         for x,y in [[a-1,b],[a,b+1],[a+1,b],[a,b-1]]:
#             if 0<=x<row and 0<=y<col and grid[x][y]==1:
#                 q.append([x,y])
#                 grid[x][y]=0
#     return count
                