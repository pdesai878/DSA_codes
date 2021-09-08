from collections import deque
class Node:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
        
class BT:
    def __init__(self):
        self.root=None
        
    def insert_level_order(self,node,arr,i):
        if i<len(arr):
            node=Node(arr[i])
            if i==0:
                self.root=node
            node.left=self.insert_level_order(node.left,arr,2*i+1)
            node.right=self.insert_level_order(node.right,arr,2*i+2)
            return node
            
            
    def create_tree_from_arr(self,arr):
        i=0 
        self.insert_level_order(self.root,arr,i)
      
        
    def level_order(self,root):
        q=deque()
        q.append(root)
        while q:
            node=q.popleft()
            print(node.val,end=" ")
            if node.left:q.append(node.left)
            if node.right:q.append(node.right)
            
             
tree=BT()
arr=[1,2,3,4,5,6,7]
tree.create_tree_from_arr(arr)
tree.level_order(tree.root)

    