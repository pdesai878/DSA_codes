class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        l=len(beginWord)
        q=deque()
        s=set(wordList)
        q.append(beginWord)
        level=1
        while q:  
            level+=1
            n=len(q)
            while n:
                word=q.popleft()
                if word in s:
                    s.remove(word)
                word=list(word)
                for i in range(l):
                    temp=word[i]
                    for ch in range(97,123):
                        if chr(ch)==temp:
                            continue
                        word[i]=chr(ch)
                        modi="".join(word)
                        if modi in s:
                            q.append(modi)
                        if modi==endWord:
                            return level
                    word[i]=temp
                                     
                n-=1
        return 0
                
            
        
        