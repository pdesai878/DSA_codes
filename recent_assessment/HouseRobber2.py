class Solution:
    def rob(self, nums: List[int]) -> int:
#         def maxmoney(n,arr,dp):
#             if n<=0: return 0 
#             if dp[n]!=-1:return dp[n]
#             #inc  #not inc                    
#             dp[n]=max(arr[n-1]+maxmoney(n-2,arr,dp),maxmoney(n-1,arr,dp))
#             return dp[n]
        
#         m=len(nums)
#         if m==1: return nums[0]
#         #if we inc last element we cant include first el
#         dp=[-1 for i in range(m+1)]
#         inclast=maxmoney(m-1,nums[1:],dp)
#         dp=[-1 for i in range(m+1)]
#         ninclast=maxmoney(m-1,nums[:],dp)
#         print(inclast,ninclast)
#         return max(inclast,ninclast)

#space optimised approach
#space optimised approach
        def maxmoney(l,r):
            prev=curr=0
            for i in range(l,r):
                res=max(prev+nums[i],curr)
                prev=curr
                curr=res
            return res
            
        n=len(nums)
        if n==1: return nums[0]
        return max(maxmoney(0,n-1),maxmoney(1,n))
        