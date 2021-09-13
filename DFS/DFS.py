#dfs algo applied on undirected graph
from collections import defaultdict
class Graph:
	def __init__(self):
		self.adjlist=defaultdict(list)

	def add_edge(self,frm,to):
		self.adjlist[frm].append(to)
		self.adjlist[to].append(frm)

	def dfs_iterative(self,src):
		visited={i:False for i in self.adjlist}
		stack=[]
		stack.append(src)
		visited[src]=True
		while stack:
			node=stack.pop()
			print(node,end=" ")
			for neighbor in self.adjlist[node]:
				if not visited[neighbor]:
					stack.append(neighbor)
					visited[neighbor]=True

	def dfs_recursive(self,src):
		def dfs_util(node):
			visited[node]=True
			print(node,end=" ")
			for neighbor in self.adjlist[node]:
				if not visited[neighbor]:
					dfs_util(neighbor)

		visited={i:False for i in self.adjlist}
		# dfs_util(src)

		#if by chance the graph contains diconnected components:
		for node in self.adjlist:
			if not visited[node]:
				dfs_util(node)


graph=Graph()
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,4)
graph.add_edge(4,5)
graph.add_edge(5,6)
graph.add_edge(3,7)
graph.add_edge(7,9)
print("dfs iterative: ")
graph.dfs_iterative(1)
print("\ndfs recursiuve: ")
graph.dfs_recursive(1)





