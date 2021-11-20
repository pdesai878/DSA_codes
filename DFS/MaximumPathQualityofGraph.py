"""
There is an undirected graph with n nodes numbered from 0 to n - 1 (inclusive). You are given a 0-indexed integer array values where values[i] is the value of the ith node. You are also given a 0-indexed 2D integer array edges, where each edges[j] = [uj, vj, timej] indicates that there is an undirected edge between the nodes uj and vj, and it takes timej seconds to travel between the two nodes. Finally, you are given an integer maxTime.

A valid path in the graph is any path that starts at node 0, ends at node 0, and takes at most maxTime seconds to complete. You may visit the same node multiple times. The quality of a valid path is the sum of the values of the unique nodes visited in the path (each node's value is added at most once to the sum).

Return the maximum quality of a valid path.

Note: There are at most four edges connected to each node.



"""

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        def dfs(value,node,maxtime):
            if maxtime<0:
                return 
            
            visited[node]+=1
            
            if visited[node]==1:
                value+=values[node]
                
            if node==0:
                self.mx=max(self.mx,value)
               
            for neighbor,time in adj[node]:
                dfs(value,neighbor,maxtime-time)
            visited[node]-=1
        
        adj=defaultdict(list)
        
        n=len(values)
        visited={i:False for i in range(n)}
        for u,v,time in edges:
            adj[u].append([v,time])
            adj[v].append([u,time])
            
        self.mx=0
        dfs(0,0,maxTime)
        return self.mx
        
                
                
            
        