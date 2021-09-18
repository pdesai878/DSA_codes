def find_max_price(n,capacity):
	if n==0 or capacity==0: return 0 
	if dp[n][capacity]!=-1:
		return dp[n][capacity]
	if length[n-1]<=capacity:
		dp[n][capacity]=max(price[n-1]+find_max_price(n,capacity-length[n-1]), find_max_price(n-1,capacity))
	else:
		dp[n][capacity]=find_max_price(n-1,capacity)
	return dp[n][capacity]


length=[1,2,3,4,5,6,7,8]
price=[1,5,8,9,10,17,17,20]
n=8

#capacity=n
#wt=length
#val=price

dp=[[-1 for j in range(n+1)] for i in range(n+1)]  

#passing length=n (capac) and index of arr. i.e last pos 
print(find_max_price(n,n))