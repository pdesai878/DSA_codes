
def is_subset_sum_possible(n,target):
    if target==0:
        return True
    if n==0 and target!=0:
        return False
    if dp[n][target]!=-1:
        return dp[n][target]
    if target>=A[n-1]:
        dp[n][target]=is_subset_sum_possible(n-1,target-A[n-1]) or is_subset_sum_possible(n-1,target)
    else:
        dp[n][target]=is_subset_sum_possible(n-1,target)
    return dp[n][target]



A=[2,4,2,3]
s=sum(A)
n=len(A)
if n==1:return A[0]
dp=[[-1 for j in range(s+1)] for i in range(n+1)]


ans=is_subset_sum_possible(n,s)  #this function basically returns if a subset is possible in the array whose sum is equal to target

mn=s

for i in range(s//2,-1,-1):
    if dp[n][i]:
        mn=s-(2*i)
        break
return mn


