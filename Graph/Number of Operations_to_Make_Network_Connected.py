#1319
'''
if there are n nodes present, there should be atleast n-1 edges present.
   Threfore, the base case would be if no_ofconnections<n-1 => return -1
now we need to find the no of isolated nodes. Since there exits a cable connection already between components,
your ans would be noofconnectedcomponents-1
'''

def dfs(node):
    visited[node]=True
    for neighbor in adjlist[node]:
        if not visited[neighbor]:
            dfs(neighbor)  

if len(connections)<n-1:
    return -1
adjlist=defaultdict(list)

for u,v in connections:
    adjlist[u].append(v)
    adjlist[v].append(u)

visited={i:False for i in range(n) }

count=-1
for node in range(n):
    if not visited[node]:
        dfs(node)
        count+=1
return count

 


