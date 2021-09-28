m=(10**9)+7
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        @lru_cache(None)
        def solve(face,s,throws):
            if s==0 and throws==0: 
                return 1
            if s<0 or throws==0: return 0        
            ans=0
            for i in range(1,face+1):
                ans+=solve(face,s-i,throws-1)
            return ans
 
        return solve(f,target,d)%m
            