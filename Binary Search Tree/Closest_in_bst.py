class Node:
	def __init__(self,value):
		self.val=value
		self.left=None
		self.right=None

def find_closest(root,target):
	diff=abs(root.val-target)
	res=root

	while root:
		if target<root.val:
			root=root.left
		elif target>root.val:
			root=root.right
		else:
			return root.val

		if root:
			d=abs(root.val-target)
			if d<diff:
				diff=d 
				res=root

	return res.val


root=Node(8)
root.left=Node(3)
root.right=Node(10)
root.left.left=Node(1)
root.left.right=Node(6)
root.left.right.left=Node(4)
root.left.right.right=Node(7)
root.right.right=Node(14)
root.right.right.left=Node(13)

print(find_closest(root,16))




