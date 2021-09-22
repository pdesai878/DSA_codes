
"""
 you need to find indexes a,b,c,d such that a<b<c<d
 and nums[a]+nums[b]+nums[c]=nums[d] --->1
 
 ==> simplifying 1 further:
 nums[a]+nums[b]=nums[d]-nums[c] where a<b<c<d
 so now we need to find pairs (a,b) & (c,d).
 
 to get nums[d]-nums[c] equal to nums[a]+nums[b],
 we ned to start exploring from right index.
 
 for each pair c,d you will update the freq in map storing (nums[d]-nums[c]).
 
 now if you find a,b such that nums[a]+nums[b] already exists in map, then no. of quadruplets would be equal to freq of (nums[d]-nums[c]), so we will add this freq to our result.
 
 will repeat the same process if you find another such pair. sum(a,b)==diff(d,c)  
"""
from collections import defaultdict
nums=[1,1,1,3,5]
dicti=defaultdict(int)
n=len(nums)
res=0
for i in range(n-1,-1,-1):
     
        
    #(a,b) pair
    for j in range(i-1,-1,-1):
        print("ab",i,j)
        if nums[i]+nums[j] in dicti:
            res+=dicti[nums[i]+nums[j]]
    print("res",res)
    print(dicti)
    #(c,d) pair
    for j in range(n-1,i,-1):
        print("cd",j,i)
        dicti[nums[j]-nums[i]]+=1
    print(dicti)
   
print(res)

# TC= O(n^2)
    

    
