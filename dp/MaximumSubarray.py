class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

#Brute force O(n^3)

        # mx=-sys.maxsize-1
        # n=len(nums) 
        # for i in range(n):
        #     for j in range(i,n):
        #         #subarray sum
        #         s=0
        #         for k in range(i,j+1):
        #             s+=nums[k] 
        #         if s>mx: mx=s
        # return mx
         
#Brute force O(n^2)           
        # mx=-sys.maxsize-1
        # n=len(nums) 
        # for i in range(n):
        #     s=nums[i]
        #     mx=max(mx,s)
        #     for j in range(i+1,n):
        #         s+=nums[j] 
        #         if s>mx: mx=s
        # return mx          
        

 """
divide and conquer algo, we divide nums into two parts:
there arises 3 cases:
1) mss lies completely in the left part
2) mss lies completely in the right part
3) mss starts from left part and ends in right part

we need to return max of the above cases

nums=[1,-2,2,3]
algo, we keep on dividing untill one el left (and that is mss itself)

==> 1,-2                                2,3
==> mssleft=1                       mssleft=2
    mssright=-2                     mssright=3
    mssincmid=-1                    mssincmid=5
    finalmss=max(1,-2,-1)=1         finalmss=max(2,3,5)=5
==> 1,-2,2,3
    mssleft=1
    mssright=5
    mssincmid=1+5
    finalmss=6
    
TC: O(nlogn)
SC: O(1)
        
        """     
        
        # def dc(l,r):
        #     if l > r:
        #         return -sys.maxsize
        #     mid = (l + r) // 2
        #     left = dc(l, mid - 1)
        #     right = dc(mid + 1, r)
        #     left_suffix_max_sum = right_prefix_max_sum = 0
        #     sum = 0
        #     for i in reversed(range(l, mid)):
        #         sum += nums[i]
        #         left_suffix_max_sum = max(left_suffix_max_sum, sum)
        #     sum = 0
        #     for i in range(mid + 1, r + 1):
        #         sum += nums[i]
        #         right_prefix_max_sum = max(right_prefix_max_sum, sum)
        #     cross_max_sum = left_suffix_max_sum + right_prefix_max_sum + nums[mid]
        #     return max(cross_max_sum, left, right)       
            
        # return dc(0,len(nums)-1)



# DP O(n) time space is implicit recursion call stack        
        # self.mx=-sys.maxsize-1
        # def solve(n):
        #     if n==0: return 0
        #     res=max(nums[n-1]+solve(n-1),nums[n-1])
        #     self.mx=max(self.mx,res)
        #     return res
        
        # solve(len(nums))
        # return self.mx


# DP O(n) time and space 
        # n=len(nums)
        # res=-sys.maxsize-1
        # dp=[-1]*(n+1)
        # dp[0]=0
        # for i in range(1,n+1):
        #     dp[i]=max(nums[i-1]+dp[i-1],nums[i-1])
        #     res=max(res,dp[i])
        # return res
        

# DP principle O(n) in O(1) space: i.e using the previously calculated result to calc curr result.       
        # n=len(nums)
        # s=0
        # mx=-sys.maxsize-1
        # for i in range(n):
        #     s=max(s+nums[i],nums[i])
        #     mx=max(mx,s)
        # return mx
           
           
               

    
        