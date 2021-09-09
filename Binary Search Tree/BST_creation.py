class Node:
	def __init__(self,value):
		self.val=value
		self.left=None
		self.right=None

def inorder(root):
	stack=[]
	node=root
	while stack or node:
		if node:
			stack.append(node)
			node=node.left
		else:
			node=stack.pop()
			print(node.val,end=" ")
			node=node.right

def insert(node,key):
	if not node:
		return Node(key)
	if key<node.val:
		node.left=insert(node.left,key)
	else:
		node.right=insert(node.right,key)
	return node

def search(root,key):
	while root:
		if key<root.val:
			root=root.left
		elif key>root.val:
			root=root.right
		else:
			return True
	return False
	

root=None
arr=[8,3,10,1,6,14,4,7,13]
for el in arr:
	root=insert(root,el)

print("inorder traversal of bst: ")
inorder(root)

#check whether an element is present in bst or not
print("\nsearching in bst:",search(root,13))


