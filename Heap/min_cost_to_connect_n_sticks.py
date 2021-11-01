import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int: 
        heap=[]
        for el in sticks:
            heapq.heappush(heap,el)
        res=0
        while len(heap)>1:
            l1=heapq.heappop(heap)
            l2=heapq.heappop(heap)
            cost=l1+l2
            res+=cost
            heapq.heappush(heap,cost)
        return res
            
            
        
        