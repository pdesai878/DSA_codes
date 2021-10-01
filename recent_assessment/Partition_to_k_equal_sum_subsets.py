class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:     
        def solve(k,su=0,ind=0):
            if k==1:
                return True
            
            if su==required_sum:
                return solve(k-1)
            if su>required_sum:
                return False    
            
            for i in range(ind,len(nums)):
                if not visited[i]:
                    visited[i]=True
                    if solve(k,su+nums[i],i+1):
                        return True
                    visited[i]=False
            return False
                
        
        #it is possible to partition arr into k subsets with equal sum iff , k divides sum(arr).
        s=sum(nums)
        if s%k!=0:
            return False
      
        required_sum=s/k
        n=len(nums)
        visited=[False]*n
        return solve(k)
        
        
        