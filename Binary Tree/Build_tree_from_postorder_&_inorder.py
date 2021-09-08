class Node:
	def __init__(self,value):
		self.val=value
		self.left=None
		self.right=None

class BT:
	def __init__(self):
		self.root=None

	def buildtree(self,postorder,inorder):
		if not inorder or not postorder:
			return None
		root=Node(postorder[-1])  #due to (root left right) order
		#find index of root in the inorder
		mid=inorder.index(root.val)

		root.left= self.buildtree(postorder[:mid],inorder[:mid])
		root.right=self.buildtree(postorder[mid:-1],inorder[mid+1:])

		return root

	def inorder(self,node):
		if not node:
			return
		self.inorder(node.left)
		print(node.val,end=" ")
		self.inorder(node.right)

	def postorder(self,root):
		stack=[]
		res=[]
		node=root
		while stack or node:
			if node:
				stack.append(node)
				res.append(node.val)
				node=node.right
			else:
				node=stack.pop()
				node=node.left
		print(*res[::-1])


tree=BT()
inorder=[9,3,15,20,7]
postorder=[9,15,7,20,3]
tree.root=tree.buildtree(postorder,inorder)

#verification
print("inorder:")
tree.inorder(tree.root)
print("\npostorder:")
tree.postorder(tree.root)
