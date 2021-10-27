# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p=l1
        q=l2
        curr=ListNode(0)
        head=curr
        carry=0
        while p or q:
            n1=p.val if p else 0
            n2=q.val if q else 0
            s=n1+n2+carry
            carry=s//10 
            curr.next=ListNode(s%10)
            curr=curr.next
            
            if p:
                p=p.next
            if q:
                q=q.next
        if carry:
            curr.next=ListNode(carry)
        return head.next
        
            
        