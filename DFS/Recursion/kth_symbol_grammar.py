class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def getval(n,k):
            if n==1 or k==1:
                return 0
            mid=math.pow(2,n-1)//2
            if k<=mid:
                return getval(n-1,k)
            else:
                return 1^getval(n-1,k-mid)
        
        return getval(n,k)
        