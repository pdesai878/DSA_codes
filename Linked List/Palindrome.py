# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        return l==l[::-1]
        
*****************************************************************
O(1) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #first find middle el with fast and slow pointer
        #reverse remaining list
        #start a dummy node from head and slow from middle.next
        #start comparing values
        
        def reverse(h):
            prev=None
            curr=h
            ans=h
            while curr:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            return prev
        
        if head.next is None:
            return True
        
        fast=head.next
        slow=head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        
        slow.next=reverse(slow.next)
      
      
        d=head
        slow=slow.next
       
        while d and slow and d.val==slow.val:
            
            d=d.next
            slow=slow.next
        
        
        if slow is None:
            return True
        
        return False
        
            
        
        