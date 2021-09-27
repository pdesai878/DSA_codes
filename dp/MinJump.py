"""
JUMP GAME 1
HERE WE NEED TO FIND OUT IF WE CAN REACH N-1 FROM 0TH INDEX.
RETURN T/F

"""


# backtracking/recursion O(2^n)
#top down dp O(n^2) becaz we are exploring each position upto max pos it can get i.e O(n * n)
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

"""
JUMP GAME 2
HERE WE NEED TO FIND OUT MIN NO OF JUMPS TO REACH N-1 FROM 0.
"""

#DP O(n^2)
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         def solve(pos):
#             if pos>=n-1: return 0
#             if dp[pos]!=-1: return dp[pos]
#             temp=n-1-pos #maxmoves from curr pos
#             mxpos=pos+nums[pos] #max pos we can get from curr pos
#             for i in range(pos+1,mxpos+1):
#                 temp=min(temp,1+solve(i))
#             dp[pos]=temp
#             return temp
#         n=len(nums)
#         dp=[-1 for i in range(n)]
#         return solve(0)
                
# Greedy approach would be, at current index make max jump and explore indexes between curr index and max index we can reach. choose out of these and update the maxreach and jump.
class Solution:
    def jump(self, nums: List[int]) -> int:
        #greedy
        n=len(nums)
        maxreach=curr_reach=jumps=0
        for i in range(n-1):
            if i+nums[i]>maxreach:
                maxreach=i+nums[i]
            if i==curr_reach:
                jumps+=1
                curr_reach=maxreach
        return jumps
            
        
                
            
               
        