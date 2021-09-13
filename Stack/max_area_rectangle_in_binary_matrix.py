def mah(arr): #O(n) 
	n=len(arr)
	mxarea=0
	stack=[]
	for i in range(n+1):
		while stack and (i==n or arr[stack[-1]]>=arr[i]):
			height=arr[stack[-1]]
			stack.pop()
			if stack:
				width=i-stack[-1]-1
			else:
				width=i 
			mxarea=max(mxarea,height*width)
		stack.append(i)
	return mxarea

matrix=[[0,1,1,0],
	[1,1,1,1],
	[1,1,1,1],
	[1,1,0,0]]

area=0
temp=[0]*len(matrix[0])
for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		if matrix[i][j]==0:temp[j]=0
		else: temp[j]+=1 
	area=max(area,mah(temp))


print(area)



