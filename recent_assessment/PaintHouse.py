class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        def solve(n,flag):
            if n==0:
                return 0 
            if (n,flag) in dp:
                return dp[(n,flag)]
            s=costs[n-1][flag]
            if flag==0:
                s+=min(solve(n-1,1),solve(n-1,2))
            elif flag==1:
                s+=min(solve(n-1,0),solve(n-1,2))
            elif flag==2:
                s+=min(solve(n-1,0),solve(n-1,1))
            dp[(n,flag)]=s   
            return s
        
        n=len(costs)
        dp={}
        temp=min(solve(n,0),solve(n,1),solve(n,2))
        return temp
        
        