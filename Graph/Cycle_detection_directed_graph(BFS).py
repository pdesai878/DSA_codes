"""
Algorithm applied is kahn's algo for topological sort. It uses BFS approach.
Topological sort of a directed cyclic graph is not possible. And hence, this algo helps determine whether our directed graph
conrtains a cycle or not.

Steps:
1. get indegree of all nodes while making connections i.e while creating a directed edge.
2. append all those nodes in the queue whose indegree is 0.
3. While processing bfs, everytime we explore the neighbors of currently popped out ndde from the queue, 
   we decreement the indegree of the neighbor as well. if indegree of neighbor becomes 0. we add the neighbor in the queue.
4. While popping out the node from queue, increement count variable.
4. while loop breaks when the queue becomes empty.
5. check whether count==#nodes in graph. if not equal it means that there exists a cycle
"""

for u,v in edges:
	adj[u].append(v)
	indegree[v]+=1
q=deque()
for node in range(n):
	if indegree[node]==0:
		q.append(node)
count=0
while q:
	node=q.popleft()
	count+=1
	for neighbor in adj[node]:
		indegree[neighbor]-=1
		if indegree[neighbor]==0:
			q.append(neighbor)
if count==n:
	print("cycle does not exists")
else:
	print("cycle exists")

