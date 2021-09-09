from collections import deque
arr=[1,2,3,1,4,5,2,3,6]
k=3
q=deque()
i=0
for j in range(len(arr)):
	while q and q[-1]<arr[j]:
		q.pop()
	q.append(arr[j])

	if j-i+1==k:
		print(q[0],end=" ")
		if q[0]==arr[0]:
			q.popleft()
		i+=1
