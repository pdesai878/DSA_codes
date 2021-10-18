def getpivot(s,e):
	pivot=s+(e-s)//2

	while s<=e:
		while arr[s]<arr[pivot]:
			s+=1
		while arr[e]>arr[pivot]:
			e-=1
		if s<=e:
			arr[s],arr[e]=arr[e],arr[s]
			s+=1
			e-=1

	return s-1

def quicksort(s,e):
	if s<e:
		ind=getpivot(s,e)
		quicksort(s,ind-1)
		quicksort(ind+1,e)
	

arr=[5,4,3,2,1,8,7,6]
quicksort(0,len(arr)-1)
print(arr)