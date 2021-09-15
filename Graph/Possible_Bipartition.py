"""
You are given a dislike array where each el is a pair (ai,bi). Now a pair means that they both dislike each other.
You need to form a group of 2 such that the pairs occur dont occur in the same group.

How can we achieve this? 
Concept of Bipartite graph: Each vertex can be divided into two distinct sets such that there exists no edge between the two sets.
How can we find out that the given graph is a bipartite graph?
-> Try to color the graph with two colors such that no adjacent vertex have same color.
Approach: DFS/BFS
Try to color the node with color 1 and neighbors of node with color 2.
While coloring if at any point you find out that the neighbor's color is the same as the node's color, we can say that the given graph is not bipartite.
==> In context to the question: If you find a conflicting edge, then it means its not possible to divide pairs into 2 groups. hence return False else True.
"""
def dfs(node,c):
    color[node]=c
    
    for neighbor in adj[node]:
        
        if color[neighbor] is None:
            if dfs(neighbor,1-c):
                return True
            
        elif color[neighbor]==color[node]:
            return True
        
    return False
        
adj=defaultdict(list)
for u,v in dislikes:
    adj[u].append(v)
    adj[v].append(u)
    
color={i:None for i in range(1,n+1)}
for node in range(1,n+1):
    if color[node] is None:
        res=dfs(node,1)
        if res:return False   #conflicting edge is present

return True