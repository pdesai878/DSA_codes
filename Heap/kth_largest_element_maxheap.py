class MaxHeap:
    def __init__(self,arr):
        self.heap=arr
        self.heapsize=len(arr)
        i=(self.heapsize-1)//2
        while i>=0:
            self.heapifymax(i)
            i-=1

    def heapifymax(self,i):
        l=2*i+1
        r=2*i+2
        if l<self.heapsize and self.heap[l]>self.heap[i]:
            largest=l
        else:
            largest=i
        if r<self.heapsize and self.heap[r]>self.heap[largest]:
            largest=r
        if largest!=i:
            self.heap[largest],self.heap[i]=self.heap[i],self.heap[largest]
            self.heapifymax(largest)

    def extractmax(self):
        if self.heapsize==0:
            return -sys.maxsize-1

        mx=self.heap[0]
        if self.heapsize>1:
            self.heap[0]=self.heap[self.heapsize-1]
            self.heapifymax(0)
        self.heapsize-=1
        return mx

nums=[0,1,2,-8,12,10]
h=MaxHeap(nums)
for i in range(6):
    print(h.extractmax())
