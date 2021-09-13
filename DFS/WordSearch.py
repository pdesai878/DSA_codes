def wordsearch(op,i,j):
	if op==word:
		return True

	if len(op)>=len(word):
		return False

	visited[i][j]=True
	for x,y in [[i-1,j],[i,j+1],[i+1,j],[i,j-1]]:
		if 0<=x<r and 0<=y<c and not visited[x][y]:
			
			mila=wordsearch(op+board[x][y],x,y)
			if mila:
				return True
	visited[i][j]=False
				
	return False


# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"
board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
r=len(board)
c=len(board[0])
ans=False
visited=[[False for j in range(c)]for i in range(r)]
for i in range(r):
	for j in range(c):
		if board[i][j]==word[0]:
			if wordsearch("",i,j):
				ans=True
				break
print(ans)

