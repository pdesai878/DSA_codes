class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        for index i, we want to calc values[i]+values[j]+i-j for all j>i
        such that for index i we get max score pair.
        
        ==> values[i]+values[j]+i-j==> (values[i]+i)+(values[j]-j)
         approach: if we maintain two separate dp table 
         dp1==> at index i, it stores max of values[i]+i obtained till now
         so for curr index j, we can update max score by doing dp[i]+values[j]-j ==> after this we update dp[i]. this makes sure i<j and for current index j we are considering max till j-1.
         
         
         once we have this dp table, we can iterate from 0 to n and update the max score for each index.
         i.e at index i==> mx=max(mx,dp1[i]+values[i]-i])
        """
           #instead of maintaining dp table we can keep variables storing max of values[i]+i till now  
        
        n=len(values)
        mxl=values[0]+0
        score=mxl
        for i in range(1,n):
            score=max(score,mxl+values[i]-i)
            mxl=max(mxl,values[i]+i)
        return score
            
        
        
        """
        Brute force: O(n^2)
        """
        # mx=-sys.maxsize
        # n=len(values)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         score=values[i]+values[j]+i-j
        #         mx=max(mx,score)
        # return mx
                
        