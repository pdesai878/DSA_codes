class Node:
	def __init__(self,value):
		self.val=value
		self.left=None
		self.right=None

class BoolHeight:
	res=None
	height=None

class BT:
	def __init__(self):
		self.root=None

	def check_balanced(self,node):
		pair=BoolHeight()
		if not node:
			pair.res=True
			pair.height=0
			return pair

		l=self.check_balanced(node.left)
		r=self.check_balanced(node.right)

		pair.height=max(l.height,r.height)+1
		if l.res and r.res and abs(l.height-r.height)<=1:
			pair.res=True
		else:
			pair.res=False
		return pair


tree=BT()
tree.root=Node(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.left.right.left=Node(7)
tree.root.right.right=Node(6)
# tree.root.left.right.left.right=Node(8)
print(tree.check_balanced(tree.root).res)
