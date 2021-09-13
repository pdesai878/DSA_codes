# https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
def get_combinations(s,index):
	if s==target:
		print(comb)
		return

	if s>target:
		return

	for i in range(index,n):
		el=candidates[i]
		comb.append(el)
		get_combinations(s+el,i)
		comb.pop()



candidates = [3,2,6,7]
n=len(candidates)
candidates.sort()
target = 7
comb=[]
s=0
index=0
get_combinations(s,index)




