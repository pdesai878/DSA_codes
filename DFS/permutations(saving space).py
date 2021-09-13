def permutations(index):

	if index==len(nums):
		res.append(nums[:])
		return

	for i in range(index,len(nums)):
		nums[i],nums[index]=nums[index],nums[i]
		permutations(index+1)
		nums[i],nums[index]=nums[index],nums[i]
		
res=[]
nums=[1,2,3]
permutations(0)
print(res)
