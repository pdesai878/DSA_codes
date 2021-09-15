"""
What we can do here is simply index all the elements and then apply binary search as if we are applying
it to an arr of size n+m. 
Therefore here lower bound would be 0 and upper bound would be (n*m)-1
Start applying bs.
now to get the matrix el based on index value: row=index//m and col=index%m
return True if el found else False
"""
def search(matrix):
	n=len(matrix)
	m=len(matrix[0])

	l=0
	r=(n*m)-1

	while l<=r:
		mid=l+(r-l)//2

		row=mid//m
		col=mid%m

		if matrix[row][col]==target:
			return True

		elif target<matrix[row][col]:
			r=mid-1

		else:
			l=mid+1

	return False
            

arr=[
[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]
]
target=12
print(search(arr))
