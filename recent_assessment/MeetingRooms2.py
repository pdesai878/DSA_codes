class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # for each new meeting we need to check whether an old room can be allocated or a new room needs to be allocated.
        
        # an old room can be allocated iff there's a meeting whose ending time is less than or equal to current meeting's ending time.
        
        # We can use a min heap here. if we add all ending times to the min heap, then top would represent the min ending time. i.e meeting which will be ending first. Then we can decide on whether our current meeting can be hosted in the old room itself (meeting of most recently ending meeting. cond: end time of meeting <= start time of current meeting) or new room.
        
        n=len(intervals)
        #sort by start time
        intervals.sort()
        heap=[]
        #push ending time of first meeting.
        heapq.heappush(heap,intervals[0][1])
        
        for i in range(1,n):
            #if current meeting start time is >= mostly recently ending meeting.
            if intervals[i][0]>=heap[0]:
                heapq.heappop(heap)
                
            #whether you are occupying old room or creating a new room, u need to update room with curr ending time
            heapq.heappush(heap,intervals[i][1])
        
        #in the end len of heap is the min no of rooms required so that no meeting is delayed.
        
        #TC = O(nlogn) for sorting + in worst case we cannot occupy any single old room i.e create a new room for each meeting. O(nlogn)  for n meetings * heapifying the heap to maintain most recently ending meeting on top.
        #SC=O(n) heap
        return len(heap)
                
                
                
            
            
        
        