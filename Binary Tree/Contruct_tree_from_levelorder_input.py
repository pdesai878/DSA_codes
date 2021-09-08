from collections import deque
class Node:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
        
class BT:
    def __init__(self):
        self.root=None
    
        
    def create_tree_from_levelorder(self,arr):
        q=deque()
        self.root=Node(arr[0])
        q.append(self.root)
        i=0
        while q:
            node=q.popleft()
            i+=1 
            if i<len(arr):
                l=arr[i]
            i+=1 
            if i<len(arr):
                r=arr[i]
            if l!=-1:
                node.left=Node(l)
                q.append(node.left)
            if r!=-1:
                node.right=Node(r)
                q.append(node.right)
                
        
    def level_order(self,root):
        q=deque()
        q.append(root)
        level=0
        while q:
            level+=1
            print("level",level,": ",end=" ")
            count=len(q)
            while count:
                node=q.popleft()
                print(node.val,end=" ")
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
                count-=1
            print()
            
tree=BT()
arr=[1,2,3,4,5,-1,6,-1,-1,7,-1,-1,-1,-1,-1]
tree.create_tree_from_levelorder(arr)
tree.level_order(tree.root)

    