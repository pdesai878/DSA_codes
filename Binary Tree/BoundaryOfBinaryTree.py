# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def isleaf(node):
            if not node:
                return False
            
            if not node.left and not node.right:
                return True
            return False
        
        def getleft(node):
            curr=node.left
            while curr:
                if not isleaf(curr):
                    res.append(curr.val)
                if curr.left:
                    curr=curr.left
                else:
                    curr=curr.right
                
                
        def getleaves(node):
            if not node:
                return
            if not node.left and not node.right: 
                res.append(node.val)
                return
            getleaves(node.left)
            getleaves(node.right)
        
        def getright(node):
            curr=node
            temp=[]
            while curr:
                if not isleaf(curr):
                    temp.append(curr.val)
                    
                if curr.right:
                    curr=curr.right
                else:
                    curr=curr.left
                    
            res.extend(temp[::-1])
                       
        
        res=[]
        if not isleaf(root):
            res.append(root.val)
            
        #left
        getleft(root)
        #leaves
        getleaves(root)
        #right in reverse 
        getright(root.right)
        
        return res
        