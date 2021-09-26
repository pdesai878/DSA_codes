#code 1
class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        def check(row,start,end):
            if end-start+1!=len(word): return False
            #left-right
            j=0
            while start+j<=end and (row[start+j]==' ' or row[start+j]==word[j]): j+=1
            if j==len(word): return True

            #right-left
            j=0
            while end-j>=start and (row[end-j]==' ' or row[end-j]==word[j]): j+=1
            if j==len(word): return True
            
            return False
        
        def solve(arr):
            n=len(arr)
            m=len(arr[0])
            #check horizontally
            for i in range(n):
                j=0
                while j<m:
                    while j<m and arr[i][j]=='#':
                        j+=1
                    start=j
                    while j<m and arr[i][j]!='#':
                        j+=1
                    end=j
                    if check(arr[i],start,end-1):
                        return True
            return False
            
   
                
        # we will be looking for placing string horizontally always
        # to check vertically, we transpose the board and start looking for placing string horizontally.
        transpose=list(map(list,zip(*board)))
        return solve(board) or solve(transpose)


**************************************************************************************************************
#code 2
class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        words=[word,word[::-1]]
        n=len(word)
        for B in board,zip(*board):
            for row in B:
                q=''.join(row).split('#')
                for w in words:
                    for s in q:
                        if len(s)==n:
                            if all(s[i]==w[i] or s[i]==' ' for i in range(n)):
                                return True
        return False
        
        
                

            
                
                
                    
        
    
