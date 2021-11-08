class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmostK(k):
            d=defaultdict(int)
            i=0
            count=0
            for j in range(n):
                d[nums[j]]+=1
                while len(d)>k and i<n:
                    d[nums[i]]-=1
                    if d[nums[i]]==0:
                        d.pop(nums[i])
                    i+=1
                count+=(j-i+1)
            return count
        n=len(nums)
        return atmostK(k)-atmostK(k-1)
                    
Tc: O(4n) [since two calls made and in each call a character is accessed atmost 2 times(once by i pointer and once by j pointer i.e 2n)] ==> 0(n)              