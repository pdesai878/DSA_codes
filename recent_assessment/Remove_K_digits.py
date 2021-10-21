"""
You are given a  number and an integer k. You can remove k digits from the number such that the resultant number is the smallest.
return the smallest number obtained.
"""

# we will maintain a queue containing inc sequence of digits by deleting k elements. 

from collections import deque
def solve(arr,k):
	q=deque()
	for ind,el in enumerate(arr):
		while q and q[-1]>=int(el) and k:  #maintaining inc seq
			q.pop()
			k-=1
		
		q.append(int(el))

	while k:
		q.pop()
		k-=1

	while q and q[0]==0:
		q.popleft()

	if not q:
		return "0"

	ans=""
	while q:
		ans+=str(q.popleft())

	return ans

arr="1432219"
k=3
print(solve(arr,k))



