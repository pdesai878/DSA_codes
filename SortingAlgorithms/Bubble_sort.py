# arr=[3,1,5,4,2]
# arr=[1,2,3,4] #best case
arr=[4,3,2,1] #worst case

n=len(arr)
passes=0
totalswaps=0
for i in range(n-1):
	passes+=1
	swaps=0
	for j in range(n-i-1):
		if arr[j]>arr[j+1]:
			swaps+=1
			arr[j],arr[j+1]=arr[j+1],arr[j]
	totalswaps+=swaps
	if swaps==0:
		break
print(arr)
print("passes",passes)
print("totalswaps",totalswaps)
