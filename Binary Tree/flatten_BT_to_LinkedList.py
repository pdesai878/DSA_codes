
#flatten binary tree to linked list such that linked list is in the same order as preorder traversal
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


#O(n) space  we do r-l-root dfs and do change pointers to achieve what we want 
# prev=None
# def flatten(node):
#     global prev
#     if not node:
#         return

#     flatten(node.right)
#     flatten(node.left)

#     node.right=prev
#     node.left=None
#     prev=node

#     return node
  

#iterative approach O(n) extra space
# def flatten(node):
#     stack=[]
#     stack.append(node)
#     while stack:
#         curr=stack.pop()
#         if node.right:
#             stack.append(node.right)
#         if node.left:
#             stack.append(node.left)
#         if stack:
#             curr.right=stack[-1]
#         curr.left=None


#O(1) space [Morris traversal]
def flatten(node):
    curr=node
    prev=None
    while curr.right:
        if curr.left:
            prev=curr.left
            while prev.right:
                prev=prev.right
            prev.right=curr.right
            curr.right=curr.left

        curr=curr.right

def printtree(node):
    if not node:
        return
    print(node.val,end=" ")
    printtree(node.right)
   

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.right.right=Node(8)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.right.left=Node(6)
root.left.right.right=Node(7)

flatten(root)
printtree(root)


