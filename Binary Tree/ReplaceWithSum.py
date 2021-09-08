class Node:
	def __init__(self,value):
		self.val=value
		self.left=None
		self.right=None

class BT:
	def __init__(self):
		self.root=None

	def replace_with_sum(self,node):
		if not node:
			return 0
		if not node.left and not node.right:
			return node.val
		else:
			l=self.replace_with_sum(node.left)
			r=self.replace_with_sum(node.right)
			temp=node.val
			node.val=l+r
			return node.val+temp

	def level_order(self,root):
		q=deque()
		q.append(root)
		while q:
			node=q.popleft()
			print(node.val,end=" ")
			if node.left:q.append(node.left)
			if node.right:q.append(node.right)


tree=BT()
tree.root=Node(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.left.right.left=Node(7)
tree.root.right.right=Node(6)
tree.replace_with_sum(tree.root)
tree.level_order(tree.root)

