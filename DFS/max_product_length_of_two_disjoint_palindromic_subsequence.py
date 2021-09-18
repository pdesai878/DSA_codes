class Solution:

    def maxProduct(self, s: str) -> int:
        self.answer = 0
        def isPalindrome(word):
            l, r = 0, len(word)-1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1; r -= 1
            return True
        
        # @functools.lru_cache(None)
        def dfs(i, word, word2):
            if i >= len(s):
                if isPalindrome(word) and isPalindrome(word2):
                    self.answer = max(self.answer, len(word) * len(word2))
                return
            
            dfs(i + 1, word + s[i], word2)
            dfs(i + 1, word, word2 + s[i])
            dfs(i + 1, word, word2)
            
        dfs(0, '', '')
        
        return self.answer