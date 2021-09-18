price=[1,5,8,9,10,17,17,20]
n=8


price=[0]+price

dp=[0]*(n+1)

dp[1]=price[1]

for i in range(2,n+1):
	dp[i]=price[i]
	for j in range(1,i+1):
		dp[i]=max(dp[i],price[j]+dp[i-j])


print(dp[-1])