def find_subsets_recursion(op,ind):
	if ind==n:
		res1.append(op[:])
		return
	
	find_subsets_recursion(op+[arr[ind]],ind+1)
	find_subsets_recursion(op,ind+1)

def find_subsets_backtracking(op,ind):
	res2.append(op[:])
	for i in range(ind,n):
		op.append(arr[i])
		find_subsets_backtracking(op,i+1)
		op.pop()

	

arr=[3,4,2,7]
n=len(arr)
res1=[]
print("With recursion: ")
find_subsets_recursion([],0)
print(res1)

res2=[]
print("With backtracking: ")
find_subsets_backtracking([],0)
print(res2)