class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # if you pick an elements i then add el*its freq to our ans.
        # also if you pick el, then you cant pick el-1 and el+1 i.e values adjacent to el. [the problem boils down to house robber prob]
        # we will iterate from 0 to max(nums) and perform step1
        
        dicti=Counter(nums)  #if el does not exists in nums, its freq is 0. 
        prev=curr=res=0
        for i in range(max(dicti)+1):
            res=max(prev+ i*dicti[i], curr)
            prev=curr
            curr=res
        return res
            
        
            
        