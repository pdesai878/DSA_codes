print("O(n)")
n=36
for i in range(1,n+1):
	if n%i==0:
		print(i)


print("\nO(sqrt(n))")
i=1
while i*i<=n:
	if n%i==0:
		print(i)
		print(n//i)
	i+=1

print("\ncorrected code: O(sqrt(n)) ")
i=1
while i*i<=n:
	if n%i==0:
		print(i)
	if i!=n//i:        #this condition is necessary. if n=36, the above code will print 6 two times
		print(n//i)
	i+=1
