class Node:
	def __init__(self,value):
		self.val=value
		self.left=None
		self.right=None

#to get height,diameter pair
class hd:
	height=None
	diameter=None
	
class BT:
	def __init__(self):
		self.root=None

	def get_height(self,node):
		if not node:
			return 0
		l=self.get_height(node.left)
		r=self.get_height(node.right)
		return 1+max(l,r)

	def get_diameter(self,node):
		if not node:
			return 0
		d1=self.get_height(node.left)+self.get_height(node.right)
		d2=self.get_diameter(node.left)
		d3=self.get_diameter(node.right)
		# print(node.val,d1,d2,d3)
		return max(d1,d2,d3)

	def get_optimised_diameter(self,node):
		pair=hd()

		if not node:
			pair.diameter=0
			pair.height=0
			return pair

		left=self.get_optimised_diameter(node.left)
		right=self.get_optimised_diameter(node.right)
		
		pair.height=max(left.height,right.height)+1

		f=left.height+right.height   #diamter passing through root
		pair.diameter=max(f,left.diameter,right.diameter)
		return pair


tree=BT()
tree.root=Node(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.left.right.left=Node(7)
tree.root.right.right=Node(8)

print(f"diameter is: {tree.get_diameter(tree.root)}")
print(f"optimised diameter is: {tree.get_optimised_diameter(tree.root).diameter}")

