"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def inorder(node):
            if not node: return
            inorder(node.left)
            if self.prev:
                self.prev.right=node
                node.left=self.prev
            else:
                self.head=node
            self.prev=node
            inorder(node.right)
            
            
        if not root:
            return
        self.prev=None
        self.head=None
        inorder(root)

        # self.prev.right=self.head     ==> if you want to convert bt to circular doubly linked list
        # self.head.left=self.prev
        return self.head