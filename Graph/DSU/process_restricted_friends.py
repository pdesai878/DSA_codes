class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        def findparent(node):
            if node==parent[node]:
                return node
            parent[node]=findparent(parent[node])
            return parent[node]
        
        def check(x,y):
            px=findparent(x)
            py=findparent(y)

            for u,v in restrictions:
                pu=findparent(u)
                pv=findparent(v)
                if (pu==px and pv==py) or (pu==py and pv==px):
                    return True
            return False
            
                
                
        def union(u,v):
            u=findparent(u)
            v=findparent(v)
            if rank[u]<rank[v]:
                parent[u]=v
            elif rank[v]<rank[u]:
                parent[v]=u
            else:
                parent[v]=u
                rank[u]+=1
                
            
                
        rank,parent=dict(),dict()
        for i in range(n):
            parent[i]=i
            rank[i]=0
            
        b=[True for i in range(len(requests))]
        
        for ind,(u,v) in enumerate(requests): 
            if check(u,v): #this method checks if request is made then will it violate any restrictions
                b[ind]=False
            else:
                union(u,v)
            
            
                    
        return b
                    
       
        