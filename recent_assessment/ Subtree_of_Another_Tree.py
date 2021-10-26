# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s, t):
        def isMatch(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False

            return s.val == t.val and isMatch(s.left, t.left) and isMatch(s.right, t.right)
        
                
        if isMatch(s, t):
            return True
        if s is None:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


#approach 2: Basically we convert our tree into string representation, then just check whether substring exists in target string.

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def convert(p):
            return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"
        
        return convert(t) in convert(s)
        