class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        mx=0
        for el in nums:
            if el-1 not in s:
                count=1
                while el+1 in nums:
                    count+=1
                mx=max(mx,count)
        return mx
        