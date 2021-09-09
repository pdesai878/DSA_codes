arr=[100,80,60,70,60,75,85]
stack=[]
# stack.append([arr[0],1])
# print(stack[0][1],end=" ")
# for el in arr[1:]:
# 	val=0
# 	while stack[-1][0]<el:
# 		val+=stack.pop()[1]
# 	val+=1
# 	print(val,end=" ")
# 	stack.append([el,val])
stack.append(0)
print(1,end=" ")

for i in range(1,len(arr)):

	while stack and arr[stack[-1]]<arr[i]:
		stack.pop()

	if stack:
		print(i-stack[-1],end=" ")
	else:
		print(i+1,end=" ")
	stack.append(i)

	



