import sys
class Node:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
    
class BT:
    def __init__(self):
        self.root=None 
        self.res=-sys.maxsize-1

    def getdiameter(self,node):

        if not node:
            return 0

        left=self.getdiameter(node.left)
        right=self.getdiameter(node.right)
        
        temp=max(left,right)+1   
        f=left+right                        #for the current node mxsum path would be max(f,left,right)
        self.res=max(self.res,temp,f)       
        return temp


tree=BT()
tree.root=Node(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.left.right.left=Node(7)
tree.root.right.right=Node(8)
tree.getdiameter(tree.root)
print(tree.res)


