# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # #get length
        # length=0
        # node=head
        # while node:
        #     node=node.next
        #     length+=1
        
        # if length==n:
        #     head=head.next
        #     return head
        
        # count=0
        # node=head
        # while count<length-n-1:
        #     node=node.next
        #     count+=1
        
        # node.next=node.next.next
        
        # return head
        
        """ single pass approach using fast and slow pointers"""  
        fast=head
        while n and fast:
            fast=fast.next
            n-=1
        
        if not fast:         #this case will happen only if we want to remove first element
            return head.next
 
        slow=head
        while fast.next:
            fast=fast.next 
            slow=slow.next
        
        
        slow.next=slow.next.next
        return head
                 
            
        
        