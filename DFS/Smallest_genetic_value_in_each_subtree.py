from collections import defaultdict
class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        
        def dfs(node):
            if visited[nums[node]]==False:
                for child in adj[node]:
                    dfs(child)
                visited[nums[node]]=True
                
        n=len(parents)
        res=[1]*n
        if 1 not in nums:
            return res
        adj=defaultdict(list)
       
        for i in range(n):
            if nums[i]==1:
                node_with_one=i
            adj[parents[i]].append(i) 
        
        visited={i:False for i in range(1,11**5)}
        #we start from node with one and travel upwards
        i=node_with_one
        value_explored=1
        while i>=0:
            dfs(i)
            while visited[value_explored]:
                value_explored+=1
            res[i]=value_explored
            i=parents[i]
        return res
            