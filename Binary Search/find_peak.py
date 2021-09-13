# def find_peak(nums):
#     if len(nums)==1:
#         return 0
#     n=len(nums)
#     l=0
#     r=n-1
#     while l<=r:
#         mid=l+(r-l)//2
#         if mid>0 and mid<n-1:
#             if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
#                 return mid
#             elif nums[mid-1]>nums[mid]:
#                 r=mid-1
#             elif nums[mid+1]>nums[mid]:
#                 l=mid+1
                
#         elif mid==0:
#             if nums[mid]>nums[mid+1]:
#                 return mid
#             return mid+1
            
#         elif mid==n-1:
#             if mid>mid-1:
#                 return mid
#             return mid-1

""" A more simpler approach to write """
# 1. Since this is a bitonic array. just before the peak element, we have a subarray sorted in ascending and after the peak el, we have a subarray sorted in descending order.
# 2. we find out mid first. if mid<mid+1 ==> it implies that we are in the ascending sorted subarray, else if mid>mid+1, we are in decendingly sorted part.
# 3. possibily of finding peak ?? if mid<mid+1 ==> towards rhs i.e do l=mid+1
# if mid>mid+1==> possibility is that mid can be the peak el but we arent sure until we explore the left part. i.e do r=mid
# 4. the loop will break out when we will have single el left. i.e l==r and when this condition is met. we get our peak el.

def find_peak(arr):
    n=len(arr)
    l=0
    r=len(arr)-1
    while l<r:
        mid=l+(r-l)//2
        
        if arr[mid]>arr[mid+1]:
            r=mid
        elif arr[mid]<arr[mid+1]:
            l=mid+1
    return l

arr=[1,2,3,4,0,-1,7]
print(find_peak(arr))