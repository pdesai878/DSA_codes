def possible(no,row,col):
	for i in range(n):
		if board[i][col]==no:
			return False
		if board[row][i]==no:
			return False
		if board[3*(row//3)+i//3][3*(col//3)+i%3]==no:
			return False


	return True


def solve(board):
	for i in range(n):
		for j in range(n):
			if board[i][j]=='.':
				for no in range(1,10):
					if possible(str(no),i,j):
						board[i][j]=str(no)
						done=solve(board)
						if done: return True
						board[i][j]='.'
				return False

    
	for row in board:
		print(*row)
	return True
		

	
				







board = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

n=len(board)
solve(board)