class Node:
	def __init__(self,value):
		self.val=value
		self.left=None
		self.right=None

class LR:
	head=Node(None)
	tail=Node(None)

def tree_to_linkedlist(node):
	l=LR()

	if not node:
		l.head=l.tail=None
		return l
	

	elif not node.left and not node.right:
		l.head=l.tail=node
		return l

	elif node.left and not node.right:
		linkedlist=tree_to_linkedlist(node.left)
		linkedlist.tail.right=node

		l.head=linkedlist.head
		l.tail=node
		return l
	

	elif node.right and not node.left:
		linkedlist=tree_to_linkedlist(node.right)
		node.right=linkedlist.head
		l.head=node
		l.tail=linkedlist.tail
		return l
	

	elif node.left and node.right:
		linkedlist_left=tree_to_linkedlist(node.left)
		linkedlist_right=tree_to_linkedlist(node.right)

		linkedlist_left.tail.right=node
		node.right=linkedlist_right.head

		l.head=linkedlist_left.head
		l.tail=linkedlist_right.tail

		return l


def printll(root):
	head=root
	while head:
		print(head.val,end=" ")
		head=head.right



root=Node(4)
root.left=Node(2)
root.right=Node(6)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(5)
root.right.right=Node(7)

ll=tree_to_linkedlist(root)
printll(ll.head)
