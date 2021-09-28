class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        """
        We can get a subarray with positive product if and only if:
        1) subarr does not contain any 0
        2) contains even no of negative numbers
        
        approach: we need to keep count of first negative and index of element 0 while iterating through the nums.
This is kind of a sliding window technique;
==>if curr index el is positive and count of negative el is even: maxsubarray would be from first index of 0 if encountered before to i.
==> if curr index el is negative and count of negative el is even:
update first negative el index to i.
===> if curr index el is negative and count of negtaive el is odd:
maxsubarray would be from first negative el index to i
        """
        
        firstneg=-1
        zeropos=-1
        countneg=0
        mx=0
        for i,el in enumerate(nums):
            if el<0:
                countneg+=1
                if firstneg==-1:
                    firstneg=i
            
            if el==0:
                firstneg=-1
                countneg=0
                zeropos=i
                
            else:
                if countneg%2==0:
                    mx=max(mx,i-zeropos)
                else:
                    mx=max(mx,i-firstneg)
        return mx
            