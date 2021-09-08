class Node:
	def __init__(self,value):
		self.val=value
		self.left=None
		self.right=None

class inex:
	inc=None
	exc=None

class BT:
	def __init__(self):
		self.root=None

	def max_subset_sum(self,node):
		pair=inex()

		if not node:
			pair.inc=pair.exc=0
			return pair
		l=self.max_subset_sum(node.left)
		r=self.max_subset_sum(node.right)

		pair.inc=node.val+l.exc+r.exc
		pair.exc=max(l.inc,l.exc)+max(r.inc,r.exc)

		return pair

tree=BT()
tree.root=Node(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.left.right.left=Node(7)
tree.root.right.right=Node(6)
res=tree.max_subset_sum(tree.root)
print(max(res.inc,res.exc))


