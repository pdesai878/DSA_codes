# for an arr of size n, total subarrays = n(n+1)//2

#recusive method
def generate_subarrays(s,e):
	if e==n: return
	elif s>e: generate_subarrays(0,e+1)
	else:
		for i in range(s,e+1):
			print(arr[i],end=" ")
		print()
		generate_subarrays(s+1,e)



arr=[1,2,3,4,5]
n=len(arr)
#generate_subarrays(0,0)


#iterative method
for i in range(n):
	for j in range(i,n):
		#print subarray with startindex=i and endindex=j
		for k in range(i,j+1):
			print(arr[k],end=" ")
		print()

