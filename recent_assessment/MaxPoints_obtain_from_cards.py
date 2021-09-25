#1423. Maximum Points You Can Obtain from Cards

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
#         @lru_cache(None)
#         def getmaxscore(s,e,k):
#             if s>e: return 0
#             if k==0: return 0
#             if dp[s][e]!=-1: return dp[s][e]
        
#             dp[s][e]=max(cardPoints[s]+getmaxscore(s+1,e,k-1),cardPoints[e]+getmaxscore(s,e-1,k-1))
#             return dp[s][e]
        
        
#         n=len(cardPoints)
#         dp=[[-1 for j in range(n+1)] for i in range(n+1)]
#         return getmaxscore(0,n-1,k)
           
"""
Key idea: You can’t choose 2nd element from the beginning unless you have chosen the first one. Similarly, you can’t choose 2nd element from last unless you have chosen the last one.

only 1st K and last K elements are relevant so calculating the sums from them.

given below:
we first calculate sum of first k elements. Then try out combinations with last k elements.
for trying comb. remove last el from the first k el and add el from last.
i.e subtract k-i from sum and add n-i. 

"""
        # n=len(cardPoints)
        # front=0
        # for i in range(k):
        #     front+=cardPoints[i]
        # mx=front
        # for i in range(k):
        #     front-=cardPoints[k-i-1]
        #     front+=cardPoints[n-i-1]
        #     mx=max(mx,front)
        # return mx
            
        
"""
The problem can also be interpreted as a sliding window prob.
Why?  what we are doing is selecting elements from start and end, such that their sum is max. What if we find a subarray of size n-k whose sum is min. Then sum of k elements which we want will be the max.
therefore, final ans= sum(all el)-sum(n-k) elements


"""
        n=len(cardPoints)
        overall_sum=sum(cardPoints)
        s=0
        i=0
        window_size=n-k
        mn=overall_sum
        for j in range(n):
            s+=cardPoints[j]
            if j-i+1==window_size:
                mn=min(mn,s)
            while j-i+1>window_size:
                s-=cardPoints[i]
                i+=1
        return overall_sum-mn
    


        
            