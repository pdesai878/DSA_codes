"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.


"""


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count=0
        nums=[i%2 for i in nums]
        dicti={0:1} #dict storing freq
        dicti[0]=1
        n=len(nums)
        s=0
        for j in range(n):
            s+=nums[j]
            if s-k in dicti:
                count+=dicti[s-k]
            if s not in dicti:
                dicti[s]=1
            else:
                dicti[s]+=1
        return count
            
            
            
            