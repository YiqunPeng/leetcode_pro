# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l1 or not l2:
            return l1 or l2
        
        h, h1, h2 = ListNode(None), ListNode(None), ListNode(None)
        old_h = h
        h1.next = l1
        h2.next = l2
        
        carry = 0
        while h1.next or h2.next:
            v1 = h1.next.val if h1.next else 0
            v2 = h2.next.val if h2.next else 0
            
            s = v1 + v2 + carry
            if s > 9:
                s -= 10
                carry = 1
            else:
                carry = 0
                
            node = ListNode(s)
            h.next = node
            h = h.next
            
            h1 = h1.next if h1.next else h1
            h2 = h2.next if h2.next else h2
        
        if carry:
            node = ListNode(1)
            h.next = node
            
        return old_h.next
   