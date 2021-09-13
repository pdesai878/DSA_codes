def bs(arr,key,findfirstpos):
	l=0
	r=len(arr)-1
	res=-1
	while l<=r:
		mid=l+(r-l)//2
		if arr[mid]==key:
			res=mid
			if findfirstpos:
				r=mid-1
			else:
				l=mid+1	
		elif key<arr[mid]:
			r=mid-1 
		else:
			l=mid+1
	return res

def first_and_last_pos(arr,key):
	first=bs(arr,key,True)
	second=bs(arr,key,False)
	return first,second


arr=[1,2,4,4,4,6]
print(first_and_last_pos(arr,4))