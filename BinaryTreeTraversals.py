from collections import deque
class Node:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
        
class BT:
    def __init__(self):
        self.root=None
    
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.val,end=" ")
            self.inorder(node.right)
            
    def preorder(self,node):
        if node:
            print(node.val,end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
            
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val,end=" ")
        
    def levelorder(self,root):
        q=deque()
        q.append(root)
        while q:
            node=q.popleft()
            print(node.val,end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
                
    def inorder_iterative(self,root):
        node=root
        stack=[]
        while stack or node:
            if node:
                stack.append(node)
                node=node.left
            else:
                node=stack.pop()
                print(node.val,end=" ")
                node=node.right
     
    def preorder_iterative(self,root):
        node=root
        stack=[]
        while stack or node:
            if node:
                stack.append(node)
                print(node.val, end=" ")
                node=node.left
            else:
                node=stack.pop()
                node=node.right
    
    def postorder_iterative(self,root):
        stack=[]
        res=[]
        node=root
        while stack or node:
            if node:
                stack.append(node)
                res.append(node.val)
                node=node.right
            else:
                node=stack.pop()
                node=node.left
                
        print(*res[::-1])
    
    def vertical_order_recursive(self,root):
        def traverse(node,dist):
            if node:
                if dist not in dicti:
                    dicti[dist]=[node.val]
                else:
                    dicti[dist].append(node.val)
                traverse(node.left,dist-1)
                traverse(node.right,dist+1)
        
        dicti={}
        dist=0
        traverse(root,dist)
        line=0
        for i in sorted(dicti):
            line+=1 
            print("line",line,": ",*dicti[i])
            
    def vertical_order_iterative(self,root):
        q=deque()
        q.append([root,0])
        dicti={}
        while q:
            node,dist=q.popleft()
            if dist not in dicti:
                dicti[dist]=[node.val]
            else:
                dicti[dist].append(node.val)
            
            if node.left: q.append([node.left,dist-1])
            if node.right:q.append([node.right,dist+1])
            
        line=0
        for i in sorted(dicti):
            line+=1 
            print("line",line,": ",*dicti[i])
            
            
    def top_view_recursive(self,root):
        
        def traverse(node,dist,level):
            if node:
                if dist not in dicti:
                    dicti[dist]=[node.val,level]
                else:
                    level_sofar=dicti[dist][1]
                    if level<level_sofar:
                        dicti[dist]=[node.val,level]
                        
                traverse(node.left,dist-1,level+1)
                traverse(node.right,dist+1,level+1)
        
        dicti={}
        dist=level=0
        traverse(root,dist,level)
        
        for i in sorted(dicti):
            print(dicti[i][0],end=" ")
    
    
    def top_view_iterative(self,root):
        q=deque()
        dicti={}
        # add root,distance,level to the queue
        q.append([root,0,0])
        
        while q:
            node,dist,level=q.popleft()
            if dist not in dicti:
                dicti[dist]=[node.val,level]
            else:
                level_sofar=dicti[dist][1]
                if level<level_sofar:
                    dicti[dist]=[node.val,level]
                    
            if node.left: q.append([node.left,dist-1,level+1])
            if node.right: q.append([node.right,dist+1,level+1])
        
        for i in sorted(dicti):
            print(dicti[i][0], end=" ")
    
    
    def bottom_view_recursive(self,root):
        
        def traverse(node,dist,level):
            if node:
                if dist not in dicti:
                    dicti[dist]=[node.val,level]
                else:
                    level_sofar=dicti[dist][1]
                    if level>level_sofar:
                        dicti[dist]=[node.val,level]
                        
                traverse(node.left,dist-1,level+1)
                traverse(node.right,dist+1,level+1)
        
        dicti={}
        dist=level=0
        traverse(root,dist,level)
        
        for i in sorted(dicti):
            print(dicti[i][0],end=" ")
    
    
    def bottom_view_iterative(self,root):
        q=deque()
        dicti={}
        # add root,distance,level to the queue
        q.append([root,0,0])
        
        while q:
            node,dist,level=q.popleft()
            if dist not in dicti:
                dicti[dist]=[node.val,level]
            else:
                level_sofar=dicti[dist][1]
                if level>level_sofar:
                    dicti[dist]=[node.val,level]
                    
            if node.left: q.append([node.left,dist-1,level+1])
            if node.right: q.append([node.right,dist+1,level+1])
        
        for i in sorted(dicti):
            print(dicti[i][0], end=" ")
            
    def get_height_recursive(self,node):
        if node is None:
            return 0
        
        l=self.get_height_recursive(node.left)
        r=self.get_height_recursive(node.right)
        
        return max(l,r)+1
        
    def get_height_iterative(self,root):
        q=deque()
        q.append(root)
        level=0
        while q:
            level+=1 
            count=len(q)
            while count:
                node=q.popleft()
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
                count-=1 
                
        return level
        
    def get_no_nodes_iterative(self,root):
        q=deque()
        q.append(root)
        count=0
        while q:
            node=q.popleft()
            count+=1 
            if node.left:q.append(node.left)
            if node.right:q.append(node.right)
        return count
        
    def get_no_nodes_recursive(self,node):   
        if not node:
            return 0
        l=self.get_no_nodes_recursive(node.left)
        r=self.get_no_nodes_recursive(node.right)
        return l+r+1
        
    
    def get_no_leaf_nodes_iterative(self,root):
        q=deque()
        q.append(root)
        count=0
        while q:
            node=q.popleft()
           
            if node.left:q.append(node.left)
            if node.right:q.append(node.right)
            
            if not node.left and not node.right:
                count+=1 
        return count
        
    def get_no_leaf_nodes_recursive(self,node):   
        if not node.left and not node.right:
            return 1
        l=self.get_no_leaf_nodes_recursive(node.left)
        r=self.get_no_leaf_nodes_recursive(node.right)
        return l+r
        
    def left_view_recursive(self,root):
        def traverse(node,dist,level):
            if node:
                if level not in dicti:
                    dicti[level]=[node.val,dist]
                else:
                    dist_sofar=dicti[level][1]
                    if dist<dist_sofar:
                        dicti[level]=[node.val,dist]
                traverse(node.left,dist-1,level+1)
                traverse(node.right,dist+1,level+1)
                
        dicti={}
        traverse(root,0,0)
        for i in sorted(dicti):
            print(dicti[i][0],end=" ")
    
    def left_view_iterative(self,root):
        dicti={}
        q=deque()
        q.append([root,0,0])
        while q:
            node,dist,level=q.popleft()
            if level not in dicti:
                dicti[level]=[node.val,dist]
            else:
                dist_sofar=dicti[level][1]
                if dist<dist_sofar:
                    dicti[level]=[node.val,dist]
            if node.left: q.append([node.left,dist-1,level+1])
            if node.right: q.append([node.right,dist+1,level+1])
        for i in sorted(dicti):
            print(dicti[i][0],end=" ")
            
    def right_view_recursive(self,root):
        def traverse(node,dist,level):
            if node:
                if level not in dicti:
                    dicti[level]=[node.val,dist]
                else:
                    dist_sofar=dicti[level][1]
                    if dist>dist_sofar:
                        dicti[level]=[node.val,dist]
                traverse(node.left,dist-1,level+1)
                traverse(node.right,dist+1,level+1)
                
        dicti={}
        traverse(root,0,0)
        for i in sorted(dicti):
            print(dicti[i][0],end=" ")
    
    def right_view_iterative(self,root):
        dicti={}
        q=deque()
        q.append([root,0,0])
        while q:
            node,dist,level=q.popleft()
            if level not in dicti:
                dicti[level]=[node.val,dist]
            else:
                dist_sofar=dicti[level][1]
                if dist>dist_sofar:
                    dicti[level]=[node.val,dist]
            if node.left: q.append([node.left,dist-1,level+1])
            if node.right: q.append([node.right,dist+1,level+1])
        for i in sorted(dicti):
            print(dicti[i][0],end=" ") 
            
            
    def boundary_traversal(self,root):
        
        #get left view excluding leaf
        def get_leftview(node):
            if not node:
                return
            if not node.left and not node.right:
                return
            else:
                print(node.val, end=" ")
                get_leftview(node.left)
                
        #get leaves now
        def getleaves(node):
            if not node:
                return
            if not node.left and not node.right:
                print(node.val,end=" ")
            else:
                getleaves(node.left)
                getleaves(node.right)
        
        #get right view in reverse order excluding root and leaf
        def get_rightview(node):
            if not node:
                return
            if not node.left and not node.right:
                return
            else:
                get_rightview(node.right)
                print(node.val,end=" ")
            
            
        #print
        get_leftview(root)
        getleaves(root)
        get_rightview(root.right)
        
    
    def left_view_method2_recursive(self,node):
        if not node:
            return
        
        print(node.val, end=" ")
        self.left_view_method2_recursive(node.left)
        
    def right_view_method2_recursive(self,node):
        if not node:
            return
        
        print(node.val, end=" ")
        self.right_view_method2_recursive(node.right)
        
    def diagonal_view_recursive(self,root):
        def traverse(node,height):
            if node:
                if height not in dicti:
                    dicti[height]=[node.val]
                else:
                    dicti[height].append(node.val)
                traverse(node.left,height+1)
                traverse(node.right,height)
        dicti={}
        traverse(root,0)
        diag=0
        for i in sorted(dicti):
            diag+=1
            print("Diagonal",diag,": ",*dicti[i])
     
    def diagonal_view_iterative(self,root):
        q=deque()
        q.append([root,0])
        dicti={}
        while q:
            node,height=q.popleft()
            if height not in dicti:
                dicti[height]=[node.val]
            else:
                dicti[height].append(node.val)
            if node.left:q.append([node.left,height+1])
            if node.right:q.append([node.right,height])
                
        diag=0
        for i in sorted(dicti):
            diag+=1
            print("Diagonal",diag,": ",*dicti[i])  
    
    #using postorder        
    def convert_to_mirror(self,node):
        if not node:
            return
        self.convert_to_mirror(node.left)
        self.convert_to_mirror(node.right)
        node.left,node.right=node.right,node.left
        
    def spiral_level_order(self,root):
        stack_lr=[root]
        stack_rl=[]
        while stack_lr or stack_rl:
            
            while stack_lr:
                node=stack_lr.pop()
                print(node.val,end=" ")
                if node.right:stack_rl.append(node.right)
                if node.left:stack_rl.append(node.left)
            
            while stack_rl:
                node=stack_rl.pop()
                print(node.val,end=" ")
                if node.left:stack_lr.append(node.left)
                if node.right:stack_lr.append(node.right)
                
        
                    
tree=BT()
# tree.root=Node(1)
# tree.root.left=Node(2)
# tree.root.right=Node(3)
# tree.root.left.left=Node(4)
# tree.root.left.right=Node(5)
# tree.root.left.right.right=Node(6)
# tree.root.right.right=Node(7)
# tree.root.right.right.right=Node(8)
tree.root=Node(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)



print("Inorder recursive: ")
tree.inorder(tree.root)

print("\nPreorder recursive: ")
tree.preorder(tree.root)

print("\nPostorder recursive: ")
tree.postorder(tree.root)

print("\nlevelorder: ")
tree.levelorder(tree.root)

print("\nInorder iterative: ")
tree.inorder_iterative(tree.root)

print("\nPreorder iterative: ")
tree.preorder_iterative(tree.root)

print("\nPostorder iterative")
tree.postorder_iterative(tree.root)

print("\nVertical order recursive: ")
tree.vertical_order_recursive(tree.root)

print("\nVertical order iterative: ")
tree.vertical_order_iterative(tree.root)

print("\n Top View recursive: ")
tree.top_view_recursive(tree.root)

print("\n Top View iterative: ")
tree.top_view_iterative(tree.root)

print("\n Bottom View recursive: ")
tree.bottom_view_recursive(tree.root)

print("\n Bottom View iterative: ")
tree.bottom_view_iterative(tree.root)

print("\nHeight of BT recursive: ",tree.get_height_recursive(tree.root))
print("\nHeight of BT iterative: ",tree.get_height_iterative(tree.root))

print("\nNo. of nodes in BT iterative: ",tree.get_no_nodes_iterative(tree.root))
print("\nNo. of nodes in BT recursive: ",tree.get_no_nodes_recursive(tree.root))

print("\nNo. of leaf nodes in BT iterative: ",tree.get_no_leaf_nodes_iterative(tree.root))
print("\nNo. of leaf nodes in BT recursive: ",tree.get_no_leaf_nodes_recursive(tree.root))

print("\nLeft View recursive:")
tree.left_view_recursive(tree.root)

print("\nLeft View iterative:")
tree.left_view_iterative(tree.root)

print("\nRight View recursive:")
tree.right_view_recursive(tree.root)

print("\nRight View iterative:")
tree.right_view_iterative(tree.root)

print("\nBoundary traversal: ")
tree.boundary_traversal(tree.root)

print("\nLeft view recursive method 2: ")
tree.left_view_method2_recursive(tree.root)

print("\nRight view recursive method 2: ")
tree.right_view_method2_recursive(tree.root)

print("\nDiagonal View recursive:")
tree.diagonal_view_recursive(tree.root)

print("\nDiagonal View iterative:")
tree.diagonal_view_iterative(tree.root)


# convert BT to its mirror
print("\ninorder of orig: ")
tree.inorder_iterative(tree.root)
tree2=tree
tree2.convert_to_mirror(tree2.root)
print("\ninorder of mirror: ")
tree2.inorder_iterative(tree2.root)

#spiral level order
print("\n Spiral level order: ")
tree.spiral_level_order(tree.root)

        
