class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        mxproduct=1
        mnproduct=1
        res=-sys.maxsize
        for el in nums:
            temp=mxproduct*el
            mxproduct=max(mxproduct*el,mnproduct*el,el)
            mnproduct=min(temp,mnproduct*el,el)
            res=max(res,mxproduct)
            
        return res

        # n=len(nums)
        # prod=1
        # mx=-sys.maxsize
        # for i in range(n):
        #     prod*=nums[i]
        #     mx=max(mx,prod)
        #     if prod==0:
        #         prod=1
            
        # prod=1   
        # for i in range(n-1,-1,-1):
        #     prod*=nums[i]
        #     mx=max(mx,prod)
        #     if prod==0:
        #         prod=1
        # return mx
        
        
#         n=len(nums)
#         mx=mn=r=nums[0]
        
#         for i in range(1,n):  
#             if nums[i]<0:
#                 mx,mn=mn,mx  
                
#             mx=max(mx*nums[i],nums[i])
#             mn=min(mn*nums[i],nums[i])
#             r=max(r,mx)
            
#         return r
        
            
            
        