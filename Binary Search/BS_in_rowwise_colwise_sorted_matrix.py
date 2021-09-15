arr=[
[10,20,30,40],
[15,25,35,45],
[28,29,37,49],
[33,34,38,50]
]
row=len(arr)
col=len(arr[0])
key=37
i=0
j=col-1

while i<row and j>=0:
	if key<arr[i][j]:
		j-=1
	elif key>arr[i][j]:
		i+=1
	if key==arr[i][j]:
		print(i,j)
		break
