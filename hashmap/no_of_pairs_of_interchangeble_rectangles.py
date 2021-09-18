from math import factorial 
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        def get_gcd(a,b):
            if not a:
                return b
            if not b:
                return a
            return get_gcd(a,b//a)
                
        
        dicti=dict()
        ans=0
        for l,b in rectangles:
            gcd=math.gcd(l,b)
            l/=gcd
            b/=gcd
            if (l,b) not in dicti:
                dicti[(l,b)]=1
            else:
                ans+=dicti[(l,b)]
                dicti[(l,b)]+=1
        return ans
            
                
        
        