"""
Here you are given a list of courses along with the pre-requisite course. i.e pair(course,prereq).
To complete a course you need to complete its prereq.

if [0,1] then 1-->0 How if this is the case, then you can complete the courses.
But if there is a deadlock situation wherein a course is waiting for its prereq to get completed and
in turn the preq is itself waiting for course to get completed first.

i.e i/p here is [[0,1],[1,0]]==> here there exists a cycle and you return False  

"""

#if there exists a cycle return False else True

#problem: detect cycle in a directed graph
from collections import defaultdict
def dfs(node):
	visited[node]=True
	visitedset[node]=True      # we maintain a visited for the current dfs call processing
	for neighbor in adjlist[node]:
		if not visited[neighbor]:
			cycle_mila=dfs(neighbor)
			if cycle_mila:
				return True

		elif visitedset[neighbor]: #cycle detected
			return True

	visitedset[node]=False
	return False              #in the end we get the initial state of visitedset as it was before when the dfs call was initiated

n=3
courses=[[0,1],[0,2]]
adjlist=defaultdict(list)
for u,v in courses:
	adjlist[u].append(v)

ans=False
visited={i:False for i in range(n)}
visitedset={i:False for i in range(n)}
for node in range(n):
	if not visited[node]:
		ans=dfs(node)
		if ans:
			break
print("cycle detected: therefore you cant finish up the courses") if ans else print("no cycle detected: you can finish up the courses")


