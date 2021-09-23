# union by rank and path compression ==> most efficient way to implement disjoint set

#step1 create rank and parent array

def makeset(n):
	rank,parent=dict(),dict()
	for i in range(1,n+1):
		parent[i].append(i)
		rank[i].append(0)

def findparent(node):
	if node==parent[node]:
		return node
	parent[node]=findparent(parent[node]) #to achieve path compression
	return parent[node]

def union(u,v):
	u=findparent(u)  #p1
	v=findparent(v)  #p2

	if rank[p1]<rank[p2]:
		parent[p1]=p2     #attach smaller rank guy to bigger rank guy
	elif rank[p1]>rank[p2]:
		parent[p2]=p1
	else:
		parent[v]=u      #if ranks are equal, attach anyone to anyone, rank of parent => increement by 1. This would also inc the height of tree by 1.
		rank[v]+=1

#do operations i.e union(u,v)

# if you want to find if u and v belong to the same component, we simply do 
  # return findparent[u]==findparent[v]
