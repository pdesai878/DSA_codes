#Dijkstra's algorithm Tc: O(n+e) Sc: O(n)
from collections import defaultdict
import sys
edges=[
[1,2,2],[1,4,1],[4,3,3],[2,3,4],[2,5,5],[3,5,1]
]
adj=defaultdict(list)
for u,v,wt in edges:
    adj[u].append([v,wt])
    adj[v].append([u,wt])

q=set()  # we use a set becaz, everytime we want to visit a node whose distance is min

src=1
dist={i:sys.maxsize for i in range(1,6)}
q.add((0,src))
dist[1]=0
while q:
    d,node=q.pop()    #pop method removes the first el of set
    
    for neighbor,edge_weight in adj[node]:

        if d+edge_weight<dist[neighbor]:
            dist[neighbor]=d+edge_weight
            q.add((dist[neighbor],neighbor))

print(dist)



