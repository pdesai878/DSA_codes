from collections import deque
s="aabccbcd"
dicti={i:0 for i in s}
q=deque()
for ch in s:
	dicti[ch]+=1
	if dicti[ch]==1:
		q.append(ch)
	else:
		if q:
			q.pop()	
	if q:
		print(q[0],end=" ")
	else:
		print(-1,end=" ")