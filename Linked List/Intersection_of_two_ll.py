# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:  O(n) space  Tc: O(m+n)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes=set()
        while headA:
            nodes.add(headA)
            headA=headA.next 
        while headB and headB not in nodes:
            headB=headB.next
        if headB in nodes:
            return headB
        else:
            return None

***********************************************************************************
Tc: o(1) Sc: O(2M) M=len of larger linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        a=headA
        b=headB
        while a!=b:
            a=headB if a is None else a.next
            b=headA if b is None else b.next 
        return a
        