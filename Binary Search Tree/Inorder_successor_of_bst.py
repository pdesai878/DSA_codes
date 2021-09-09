class Node:
	def __init__(self,value):
		self.val=value
		self.left=None
		self.right=None

def find_inorder_successor(root,key):
	if not root:
		return None

	res=None
	while root:
		if root.val>key.val:
			res=root.val
			root=root.left
		else:
			root=root.right
	return res


root=Node(8)
root.left=Node(3)
root.right=Node(10)
root.left.left=Node(1)
root.left.right=Node(6)
root.left.right.left=Node(4)
root.left.right.right=Node(7)
root.right.right=Node(14)
root.right.right.left=Node(13)

print(find_inorder_successor(root,root.left.right.right))
