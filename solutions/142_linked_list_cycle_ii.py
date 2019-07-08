# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        s = f = h = head
        has_cycle = False
        
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
            
            if s is f:
                has_cycle = True
                break
                
        if not has_cycle:
            return None
        
        while s is not h:
            s = s.next
            h = h.next
            
        return s