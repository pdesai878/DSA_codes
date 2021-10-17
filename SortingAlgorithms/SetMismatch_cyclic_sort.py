# 645. Set Mismatch
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
       #duplicate el would be at wrong index after cyclic sort and missing will be index+1
    
        n=len(nums)
        i=0
        while i<n:
            ind=nums[i]-1
            if nums[i]!=nums[ind]:
                nums[i],nums[ind]=nums[ind],nums[i]
            else:
                i+=1
        for i in range(n):
            if nums[i]!=i+1:
                return [nums[i],i+1]
        return []
            
            
        