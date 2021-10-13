arr=[3,1,4,2,5]

n=len(arr)
for i in range(n-1):
	min_el=min(arr[i:n])
	ind=arr.index(min_el)
	arr[ind],arr[i]=arr[i],arr[ind]
	
print(arr)
