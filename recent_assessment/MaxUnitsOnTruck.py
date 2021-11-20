class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        n=len(boxTypes)
        units=0
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        for i in range(n):
            boxCount=min(truckSize,boxTypes[i][0])
            units+=(boxCount*boxTypes[i][1])
            truckSize-=boxCount
            if truckSize==0:
                break
            
        return units
        
            
            
        