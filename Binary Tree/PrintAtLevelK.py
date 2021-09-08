from collections import deque
class Node:
	def __init__(self,value):
		self.val=value
		self.left=None
		self.right=None
class BT:
	def __init__(self):
		self.root=None

	def print_at_level_k(self,root,k):
		q=deque()
		q.append(root)
		level=0
		flag=False
		while q:
			level+=1
			if level==k:
				flag=True
				print(f"level{level}: ",end=" ")
				
			count=len(q)
			
			while count:
				node=q.popleft()
				if flag: print(node.val,end=" ")
				if node.left:q.append(node.left)
				if node.right:q.append(node.right)
				count-=1
			if flag: break
				

	# def print_at_level_k(self,node,k):
	# 	if not node:
	# 		return 

	# 	if k==1:
	# 		print(node.val, end=" ")
	# 	else:
	# 		self.print_at_level_k(node.left,k-1)
	# 		self.print_at_level_k(node.right,k-1)

tree=BT()
tree.root=Node(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.left.right.left=Node(7)
tree.root.right.right=Node(6)
tree.print_at_level_k(tree.root,2)
