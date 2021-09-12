def find_max_area_bruteforce():
	nsr=[0 for i in range(n)]
	nsl=[0 for i in range(n)]
	for i in range(n):
		el=arr[i]
		for j in range(i+1,n):
			if arr[j]<el:
				nsr[i]=j
				break
		if nsr[i]==0:
			nsr[i]=n


	for i in reversed(range(n)):
		el=arr[i]
		for j in range(i-1,0,-1):
			if arr[j]<el:
				nsl[i]=j
				break
		if nsl[i]==0:
			nsl[i]=-1


	res=[]
	mx=-1
	for i in range(n):
		area=(nsr[i]-nsl[i]-1)*arr[i]
		if area>mx:
			mx=area
		res.append(area)

	# print(nsr)
	# print(nsl)
	print("max area histogram:",mx)


def find_max_area_using_stack():
	#this approach we are storing boundaries in nsr and nsl

	nsl,nsr=[],[]
	#nsl
	stack=[]
	for i in range(n):
		if not stack:
			nsl.append(0)

		elif stack and arr[stack[-1]]<arr[i]:
			nsl.append(stack[-1]+1)

		elif stack and arr[stack[-1]]>arr[i]:
			while stack and arr[stack[-1]]>arr[i]:
				stack.pop()
			if not stack:
				nsl.append(0)
			else:
				nsl.append(stack[-1]+1)
				
		stack.append(i)


	stack=[]
	nsr=[]
	for i in reversed(range(n)):
		if not stack:
			nsr.append(n-1)

		elif stack and arr[stack[-1]]<arr[i]:
			nsr.append(stack[-1]-1)

		elif stack and arr[stack[-1]]>arr[i]:
			while stack and arr[stack[-1]]>arr[i]:
				stack.pop()
			if not stack:
				nsr.append(n-1)
			else:
				nsr.append(stack[-1]-1)
				
		stack.append(i)		
		
	nsr.reverse()

	mx=-1
	for i in range(n):
		area=(nsr[i]-nsl[i]+1)*arr[i]
		mx=max(mx,area)
	print(mx)


def find_max_area_singlepass():
	stack=[]
	area=0
	for i in range(n):
		while stack and (i==n or arr[stack[-1]]>=arr[i]):
			height=arr[stack[-1]]
			stack.pop()
			if not stack:
				width=i
			else:
				width=i-stack[-1]-1
			area=max(area,height*width)
		stack.append(i)
	print(area)

# arr=[2,1,5,6,2,3]
arr=[3,2,10,11,5,10,6,3]
print(arr)
n=len(arr)
# find_max_area_bruteforce()
# find_max_area_using_stack()
find_max_area_singlepass()





