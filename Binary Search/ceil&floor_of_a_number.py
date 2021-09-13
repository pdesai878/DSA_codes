# def find_floor_ceil(arr,key):
	# l=0
	# r=len(arr)-1
	# floor=ceil=-1
	# while l<=r:
	# 	mid=l+(r-l)//2
	# 	if arr[mid]==key:
	# 		return mid,mid
	# 	if key<arr[mid]:
	# 		ceil=arr[mid]
	# 		r=mid-1 
	# 	else:
	# 		floor=arr[mid]
	# 		l=mid+1
	# return floor,ceil

def find_floor_ceil(arr,key):
	l=0
	r=len(arr)-1
	while l<=r:
		mid=l+(r-l)//2
		if arr[mid]==key:
			return mid,mid
		if key<arr[mid]:
			r=mid-1 
		else:
			l=mid+1
	floor,ceil=arr[r],arr[l]
	return floor,ceil



arr=[2,3,5,9,14,16,18]
target=15
print(find_floor_ceil(arr,target))