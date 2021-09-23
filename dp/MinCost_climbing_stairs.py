class Solution:
def minCostClimbingStairs(self, cost: List[int]) -> int:
    """
    If we want to know the min cost to reach stair #n, It will be tremendously helpful to know the min cost to reach step #n-1 and step #n-2 (because we can reach step #n in one or two step from them)
    """
   #final cost to reach n =min(mincost to reach n-1, mincost to reach n-2)
    def mincost(n):
        if n<0: return 0
        if n==0 or n==1: return cost[n]     # we can either start from step0 or step1
        if dp[n]!=-1:return dp[n]
        
        dp[n]=cost[n]+min(mincost(n-1),mincost(n-2))
        return dp[n]
    
    n=len(cost)
    dp=[-1]*n
    return min(mincost(n-1),mincost(n-2))
        