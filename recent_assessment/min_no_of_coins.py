p=10**31-1
"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def getfewestcoins(n,s):
            if n==0 and s!=0: return p
            if s<0: return p
            if s==0: return 0
            if dp[n][s]!=-1: return dp[n][s]
            if coins[n-1]<=amount:
                dp[n][s]=min(1+getfewestcoins(n,s-coins[n-1]),getfewestcoins(n-1,s))
            else:
                dp[n][s]=getfewestcoins(n-1,s)
            return dp[n][s]
        
        n=len(coins)
        dp=[[-1 for j in range(amount+1)] for i in range(n+1)]
        ans=getfewestcoins(n,amount)
        return -1 if ans==p else ans
        
        