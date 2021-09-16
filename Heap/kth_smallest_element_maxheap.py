import sys
class MaxHeap:
	def __init__(self,arr):
		self.heap=arr
		self.heapsize=len(arr)
		i=(self.heapsize-1)//2
		#applying heapify to internal nodes
		while i>=0:
			self.maxheapify(i)
			i-=1

	def maxheapify(self,i):
		l=2*i+1
		r=2*i+2
		if l<self.heapsize and self.heap[l]>self.heap[i]:
			largest=l
		else:
			largest=i
		if r<self.heapsize and self.heap[r]>self.heap[largest]:
			largest=r 
		if largest!=i:
			self.heap[i],self.heap[largest]=self.heap[largest],self.heap[i]
			self.maxheapify(largest)

	def extractmax(self):
		if self.heapsize==0:
			return sys.maxsize

		mx=self.heap[0] 

		#move last el to the root and call heapify
		if self.heapsize>1:
			self.heap[0]=self.heap[self.heapsize-1]
			self.maxheapify(0)
		self.heapsize-=1
		return mx

#get kth smallest element out of array
arr=[2,3,5,15,-1]
k=2

if 0<k<len(arr):
	heap=MaxHeap(arr[:k])  #build heap of elements from index 0 to k. O(k)
	for i in range(k+1,len(arr)):   #O((n-k)log(k))
		if arr[i]<heap.heap[0]:
			heap.heap[0]=arr[i]
			heap.maxheapify(0)
		
	print(heap.heap[0])
else:
	print("invalid k")


#overall time complexity== O(n+klog(n))

