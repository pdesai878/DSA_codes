"""
Given a weighted graph, a spanning tree is the one containing all n nodes of graph and edges=n-1
such that every node is reachable from every other node.
Given a weighted undirected graph,
A min spanning tree is the one which will have min cost. (sum all edge weights to get cost)
"""

"""
Prims algo to find mst. 
We start from the first node. Find min edge attached to the node and connect.
Now we have 2 nodes. explore edges attached to these both nodes and connect the min of all.
Repeat the same process as you connect more and more nodes. 
"""
from collections import defaultdict
import sys
adj=defaultdict(list)

def find_min_edge_node():
	distance=sys.maxsize
	ans=None
	for node in dist:
		if not visited[node] and dist[node]<distance:
			ans=node 
			distance=dist[node]

	return ans

#create graph
n=5
edges=[[0,3,6],[0,1,2],[3,1,8],[1,4,5],[1,2,3],[4,2,7]]
for u,v,edgewt in edges:
	adj[u].append([v,edgewt])
	adj[v].append([u,edgewt])

visited={i:False for i in range(n)}
src=0
dist={src:0}
for node in range(n):
	mn=find_min_edge_node()   #min edge node
	visited[mn]=True          
	print(mn,end=" ")

	#update distance
	for neighbor in adj[mn]:
		dist[neighbor[0]]=neighbor[1]

