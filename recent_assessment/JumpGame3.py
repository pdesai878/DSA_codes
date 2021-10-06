class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def solve(n): 
                
            if 0<=n<len(arr) and arr[n]>=0:
                arr[n]=-arr[n]  #this step is to mark elements as we visit so that we dont have to process them again. We can use visited arr as well, but that would take extra space
                return arr[n]==0 or solve(n+arr[n]) or solve(n-arr[n])
            return False
        
        return solve(start)