res=[]
def solve(op,nums):
    if len(op)==len(nums):
        res.append([*op])
  
    for el in nums:

        if not dicti[el]:
            continue

        dicti[el]=False
        op.append(el)
        solve(op,nums)
        op.remove(el)
        dicti[el]=True
 

nums=[1,2,3]
dicti={i:True for i in nums}
op=[]
res=[]
solve(op,nums)
print(res)

