arr=[4,3,2,7,8,2,3,1]
res=[]
i=0
n=len(arr)
while i<n:
    ind=arr[i]-1
    if arr[i]!=arr[ind]:
        arr[i],arr[ind]=arr[ind],arr[i]
    else:
        i+=1

for i in range(n):
    if arr[i]!=i+1:
        res.append(i+1)

if arr[n-1]!=n:
    res.append(n)

print(res)