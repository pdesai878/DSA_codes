class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:

        if len(num1)>len(num2):
            return self.findMedianSortedArrays(num2,num1)

        n1=len(num1)
        n2=len(num2)
        totallen=(n1+n2)
        low=0
        high=n1

        while low<=high:
            #cut1: how many can you pick from the first arr
            cut1=low+(high-low)//2
            #cut2 will be elements you are picking from second arr
            cut2=(n1+n2+1)//2-cut1

            l1=-sys.maxsize if cut1==0 else num1[cut1-1]
            l2=-sys.maxsize if cut2==0 else num2[cut2-1]

            r1=sys.maxsize if cut1==n1 else num1[cut1]
            r2=sys.maxsize if cut2==n2 else num2[cut2]

            if l1<=r2 and l2<=r1:
                if totallen%2==0:
                    return (max(l1,l2)+min(r1,r2))/2
                return max(l1,l2)

            elif l1>r2:
                high=cut1-1
            else:
                low=cut1+1
                
        return 0
        
        
                
        
        
        