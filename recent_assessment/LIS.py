class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        mx=1
        ind=0
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
            if dp[i]>mx:
                mx=dp[i]
                ind=i
        
        q=deque()
        q.appendleft(nums[ind])
        for i in range(ind,-1,-1):
            if dp[i]+1==dp[ind] and nums[i]<nums[ind]:
                ind=i
                q.appendleft(nums[i])
                    
        print("".join(list(map(str,q))))
   
        return mx
            
            
***********************************************************

O(nlogn) approach using bs and dp
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def getceil(key):
            l=0
            r=len(seq)-1
            res=-1
            while l<=r:
                mid=l+(r-l)//2
                if seq[mid]==key:
                    return mid
                if key<seq[mid]:
                    res=seq[mid]
                    r=mid-1 
                else:
                    l=mid+1
            return l
  
        
        n=len(nums)
        seq=[]
        seq.append(nums[0])
        for i in range(1,n):
            if nums[i]>seq[-1]:
                seq.append(nums[i])
            else:
                ind=getceil(nums[i])
                seq[ind]=nums[i]
   
        return len(seq)
            
            
        