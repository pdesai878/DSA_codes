# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def getsum(node):
            if not node:
                return 0
            s=node.val+getsum(node.left)+getsum(node.right)
            d[s]+=1
            self.mx=max(self.mx,d[s])
            return s
            
            
        d=defaultdict(int)
        self.mx=-sys.maxsize
        ans=[]
        getsum(root)
        for key,value in d.items():
            if value==self.mx:
                ans.append(key)
        return ans
        