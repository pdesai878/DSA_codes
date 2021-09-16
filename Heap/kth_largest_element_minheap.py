class MinHeap:
	def __init__(self,arr):
		self.heap=arr
		self.heapsize=len(arr)
		i=(self.heapsize-1)//2
		#applying heapify to internal nodes
		while i>=0:
			self.minheapify(i)
			i-=1

	def minheapify(self,i):
		l=2*i+1
		r=2*i+2
		if l<self.heapsize and self.heap[l]<self.heap[i]:
			smallest=l
		else:
			smallest=i
		if r<self.heapsize and self.heap[r]<self.heap[smallest]:
			smallest=r 
		if smallest!=i:
			self.heap[i],self.heap[smallest]=self.heap[smallest],self.heap[i]
			self.minheapify(smallest)

	def extractmin(self):
		if self.heapsize==0:
			return sys.maxsize

		mn=self.heap[0] 

		#move last el to the root and call heapify
		if self.heapsize>1:
			self.heap[0]=self.heap[self.heapsize-1]
			self.minheapify(0)
		self.heapsize-=1
		return mn

arr=[2,1]
k=2
#find kth largest           #ans=3
h=MinHeap(arr[:k])
for el in arr[k:]:
	if el>h.heap[0]:
		h.heap[0]=el 
		h.minheapify(0)
print(h.heap[0])
