arr=[3,5,4,1,2,9,9,10]
n=len(arr)
for i in range(n-1):
	j=i+1
	while j>0:
		if arr[j]<arr[j-1]:
			arr[j],arr[j-1]=arr[j-1],arr[j]
			j-=1
		else:
			break

print(arr)