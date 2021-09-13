def find_ceil(arr,key):
	l=0
	r=len(arr)-1
	res=-1
	while l<=r:
		mid=l+(r-l)//2
		if arr[mid]==key:
			return mid
		if key<arr[mid]:
			res=arr[mid]
			r=mid-1 
		else:
			l=mid+1
	return res


arr=[2,3,5,9,14,16,18]
target=15
print(find_ceil(arr,target))