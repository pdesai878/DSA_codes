class Node:
	def __init__(self,value):
		self.val=value
		self.left=None
		self.right=None

class BT:
	def __init__(self):
		self.root=None

	def buildtree(self,preorder,inorder):
		if not inorder or not preorder:
			return None
		root=Node(preorder[0])  #due to (root left right) order
		#find index of root in the inorder
		mid=inorder.index(root.val)

		root.left= self.buildtree(preorder[1:mid+1],inorder[:mid])
		root.right=self.buildtree(preorder[mid+1:],inorder[mid+1:])

		return root

	def inorder(self,node):
		if not node:
			return
		self.inorder(node.left)
		print(node.val,end=" ")
		self.inorder(node.right)

	def preorder(self,root):
		stack=[]
		node=root
		while stack or node:
			if node:
				stack.append(node)
				print(node.val,end=" ")
				node=node.left
			else:
				node=stack.pop()
				node=node.right


tree=BT()
inorder=[9,3,15,20,7]
preorder=[3,9,20,15,7]
tree.root=tree.buildtree(preorder,inorder)

#verification
print("inorder:")
tree.inorder(tree.root)
print("\npreorder:")
tree.preorder(tree.root)
