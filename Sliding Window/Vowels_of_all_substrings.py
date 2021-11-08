#this is not actually a sliding window problem
class Solution:
    def countVowels(self, word: str) -> int:
        i=count=0
        vowels=set(['a','e','i','o','u'])
        n=len(word)
        for j in range(n):
            if word[j] in vowels:  #so you need to find and sum record contribution of a vowel in each substring it can form
                l=j+1
                r=n-j
                count+=(l*r)       
        return count
                    
        