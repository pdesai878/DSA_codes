# binary exponential is an algo to find a^b
# it follows divide and conquer strategy. 
# here main approach resides in dividing the power by 2 till it becomes 0.
# therefore base case : if b==0: return 1
# fn(a,b)==> if b is even:  make two calls. return fn(a,b//2)*fn(a,b//2)
#        ==> if b is odd:   return a*fn(a,b//2)*fn(a,b//2)
def binaryexp(a,b):
	if b==0: return 1
	res=binaryexp(a,b//2)
	if b&1: return a*((res*res)%m)%m
	return (res*res)%m


#we use binary of b. if ith bit is set we multiply current power of a to ans. 
# and each time we inc power of a and do a right shift operation on b, we continue the loop untill b
def binaryexp_iterative(a,b):
	ans=1
	while b:
		if b&1:
			ans=(ans*a)%m
		a=(a*a)%m
		b>>=1           
	return ans


m=(10**9)+7
print(binaryexp(2,19))
print(binaryexp_iterative(2,19))