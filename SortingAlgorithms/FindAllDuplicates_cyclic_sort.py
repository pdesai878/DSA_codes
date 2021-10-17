class Solution:
    def findDuplicates(self, arr: List[int]) -> List[int]:
        res=set()
        n=len(arr)
        i=0
        while i<n:
            ind=arr[i]-1
            if arr[i]!=arr[ind]:
                arr[i],arr[ind]=arr[ind],arr[i]
                continue
            elif arr[i]==arr[ind] and arr[i]!=i+1:
                res.add(arr[i])
            i+=1
        return list(res)
            
        