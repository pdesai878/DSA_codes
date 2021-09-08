from collections import defaultdict,deque
class Node:
	def __init__(self,value):
		self.val=value
		self.left=None
		self.right=None
class BT:
	def __init__(self):
		self.root=None

	def print_nodes_at_distance_k(self,root,target,k):
		def connect(node):
			if not node:
				return
			if node.left:
				adj[node].append(node.left)
				adj[node.left].append(node)
				
			if node.right:
				adj[node].append(node.right)
				adj[node.right].append(node)
			connect(node.left)
			connect(node.right)


		adj=defaultdict(list)
		connect(root)

		# for i in adj:
		# 	print(i.val,": ",end=" ")
		# 	for node in adj[i]:
		# 		print(node.val,end=" ")
		# 	print()
		q=deque()
		q.append([target,0])

		visited={target}

		while q:
			node,dist=q.popleft()
			if dist==k:
				print(node.val,end=" ")
			for neighbor in adj[node]:
				if neighbor not in visited:
					visited.add(neighbor)
					q.append([neighbor,dist+1])
			if dist>k:
				break









tree=BT()
tree.root=Node(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.left.right.left=Node(7)
tree.root.left.right.right=Node(8)
tree.root.left.right.right.left=Node(9)
tree.root.left.right.right.right=Node(10)
tree.root.right.right=Node(6)

target=tree.root.left.right
tree.print_nodes_at_distance_k(tree.root,target,2)


