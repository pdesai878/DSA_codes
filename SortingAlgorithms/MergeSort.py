# def merge(left,right):
# 	arr=[0]*(len(left)+len(right))
# 	l=r=k=0
# 	while l<len(left) and r<len(right):
# 		if left[l]<right[r]:
# 			arr[k]=left[l]
# 			l+=1
# 		else:
# 			arr[k]=right[r]
# 			r+=1
# 		k+=1

# 	while l<len(left):
# 		arr[k]=left[l]
# 		l+=1
# 		k+=1
# 	while r<len(right):
# 		arr[k]=right[r]
# 		r+=1
# 		k+=1
# 	return arr




# def mergesort(arr):
# 	n=len(arr)
# 	if n==1:
# 		return arr
# 	mid=n//2
# 	left=mergesort(arr[:mid])
# 	right=mergesort(arr[mid:])
# 	return merge(left,right)

	



arr=[8,3,4,12,5,6]
# print(mergesort(arr)) 
#note that in the above code, it is creating a new arr obj in every fn call. orig arr not modified in place!



def mergesort(s,e):
	if e-s==1:
		return
	mid=s+(e-s)//2
	mergesort(s,mid)
	mergesort(mid,e)
	return merge(s,mid,e)

def merge(s,mid,e):
	mix=[0]*(e-s)
	l=s 
	r=mid 
	k=0

	while l<mid and r<e:
		if arr[l]<arr[r]:
			mix[k]=arr[l]
			l+=1
		else:
			mix[k]=arr[r]
			r+=1
		k+=1

	while l<mid:
		mix[k]=arr[l]
		l+=1
		k+=1
	while r<e:
		mix[k]=arr[r]
		r+=1
		k+=1

	for i in range(len(mix)):
		arr[s+i]=mix[i]



#inplace sorting with mergesort    
mergesort(0,len(arr))
print(arr)
