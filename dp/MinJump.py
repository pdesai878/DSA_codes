# backtracking/recursion O(2^n)
#top down dp O(n^2)
# def solve(pos):
#     if pos==n-1: return True
#     if dp[pos]!=-1: return dp[pos]
#     max_reach=pos+nums[pos]
#     for i in range(pos+1,max_reach+1):
#         if solve(i):
#             dp[pos]=True
#             return True
#     dp[pos]=False
#     return False
     
# nums=[2,3,1,1,0,4]
# n=len(nums)
# dp=[-1 for i in range(n+1)]
# print(solve(0))

#optimised code (Greedy approach) O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mxreachable=0
        #if our current index crosses the max reachable distance, we cant reach the end.
        n=len(nums)
        for i in range(n):
            if i>mxreachable:
                return False
            mxreachable=max(mxreachable,i+nums[i])
        return True
