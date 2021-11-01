from collections import defaultdict,deque
import sys
edges=[
[0,1],[0,3],[1,2],[3,4],[1,3],[4,5],[5,6],[2,6],[6,7],[6,8],[7,8]
]
adj=defaultdict(list)
for u,v in edges:
    adj[u].append(v)
    adj[v].append(u)

q=deque()
# print(adj)
src=0
dist={i:sys.maxsize for i in range(9)}
q.append(0)
dist[0]=0
while q:
    node=q.popleft()
    for neighbor in adj[node]:
        if dist[neighbor]>dist[node]+1:
            q.append(neighbor)
            dist[neighbor]=dist[node]+1
print(dist)



