from collections import deque
class Node:
	def __init__(self,value):
		self.val=value
		self.left=None
		self.right=None

def create_bst(arr,s,e):
	if s==e:
		return Node(arr[s])
	
	mid=(s+e)//2
	node=Node(arr[mid])
	node.left=create_bst(arr,s,mid-1)
	node.right=create_bst(arr,mid+1,e)
	return node

def levelorder(root):
	q=deque()
	q.append(root)
	while q:
		node=q.popleft()
		print(node.val,end=" ")
		if node.left:q.append(node.left)
		if node.right:q.append(node.right)
		

arr=[1,2,3,4,5,6,7]
root=create_bst(arr,0,len(arr)-1)

levelorder(root)