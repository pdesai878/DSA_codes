class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[0 for j in range(n)] for i in range(n)]
        
        #check for len 1 & 2 palindromic substr
        mx=0
        st=en=0
        for i in range(n):
            dp[i][i]=1
            j=i+1
            if j<n:
                if s[i]==s[j]:
                    dp[i][j]=1      
                if dp[i][j] and j-i+1>mx:
                    mx=j-i+1
                    st=i
                    en=j
                    
        #check for len>2 palindromic substr
        
        for j in range(2,n): 
            for i in range(j-1):
                dp[i][j]=1 if s[i]==s[j] and dp[i+1][j-1] else 0
                if dp[i][j] and j-i+1>mx:
                    mx=j-i+1
                    st=i
                    en=j
              
                    
        return s[st:en+1]

**************************************************************************************************
0(1) space
import sys
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        resLen=st=en=0
        for i in range(n):
        #odd 
            l,r=i,i
            while l>=0 and r<n and s[l]==s[r]:
                if (r-l+1)>resLen:
                    resLen=r-l+1    
                    st=l
                    en=r
                l-=1
                r+=1

        #even
            l,r=i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                if (r-l+1)>resLen:
                    resLen=r-l+1    
                    st=l
                    en=r
                l-=1
                r+=1
        return s[st:en+1]
            
            
                
              
             
                
        
        
     
    

  
