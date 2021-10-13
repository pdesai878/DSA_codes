# cyclic sort can sort your array in O(n) if array contains elements in range 1 to n only.

arr=[3,1,4,2,6,5]
n=len(arr)
for i in range(n):
	if arr[i]==i+1:
		continue
	while arr[i]!=i+1:
		ind=arr[i]-1  #correct index of current el. curr el=arr[i]
		arr[i],arr[ind]=arr[ind],arr[i]

print(arr)

#time complexity= O(n)