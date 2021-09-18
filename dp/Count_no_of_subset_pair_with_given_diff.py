def count_subsets(target,n):
	if target==0:
		return 1
	if n==0 and target!=0:
		return 0
	if dp[n][target]!=-1: return dp[n][target]
	if arr[n-1]<=target:
		dp[n][target]=count_subsets(target-arr[n-1],n-1)+count_subsets(target,n-1)
	else:
		dp[n][target]=count_subsets(target,n-1)
	return dp[n][target]

arr=[1,1,2,3]
n=len(arr)
diff=1
target=(diff+sum(arr))//2
dp=[[-1 for j in range(target+1)] for i in range(n+1)]
print(count_subsets(target,n)) #no of pairs