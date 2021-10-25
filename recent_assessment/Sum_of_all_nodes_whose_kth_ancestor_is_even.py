"""
This can be solved in O(nk).
Approach:
1)Store (node,parentnode) pair in a map [ This can be achieved by doing a bfs traversal].
2)For each node, traverse k times in upwards direction and check the kth parent's value. if its even, add current node's value to sum.
"""

from collections import deque
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def getsum(root,k):
    parent={}
    #getparents
    q=deque()
    q.append(root)
    parent[root]=None
    res=[]

    while q:
        node=q.popleft()
        res.append(node)
        if node.left:
            parent[node.left]=node
            q.append(node.left)
        if node.right:
            parent[node.right]=node
            q.append(node.right)

    # to get sum
    s=0
    for node in res:
        curr=node
        count=k
        while parent[curr]:
            curr=parent[curr]
            count-=1
            if count==0 and curr:
                if curr.val%2==0:
                    s+=node.val
                    break
   
    return s


# root=Node(1)
# root.left=Node(2)
# root.right=Node(3)
# root.left.left=Node(4)
# root.left.right=Node(5)
# root.left.left.left=Node(7)
# root.right.left=Node(6)

root=Node(4)
root.left=Node(6)
root.right=Node(8)
root.left.left=Node(8)
root.left.right=Node(5)
k=2
print(getsum(root,k))     #13
