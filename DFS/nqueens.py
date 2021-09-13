def possible(row,col):
    
    #check column
    for i in range(row):
        if board[i][col]=='Q':
            return False
    
    #check left diagonal
    i=row
    j=col
    while i>=0 and j>=0:
        if board[i][j]=='Q':
            return False
        i-=1
        j-=1
    
    #check right diagonal
    i=row 
    j=col
    while i>=0 and j<n:
        if board[i][j]=='Q':
            return False
        i-=1
        j+=1
        
    return True
          


def solve(row):
    if row==3:
        temp=[]
        for r in board:
            temp.append("".join(r))
        res.append(temp)

    
    for col in range(n):
        nrow=row+1
        if possible(nrow,col):
            board[nrow][col]='Q'
            solve(nrow)
            board[nrow][col]='.'
n=4           
board=[["." for j in range(n)] for i in range(n)]
res=[]
row=-1
solve(row)
print(res)
