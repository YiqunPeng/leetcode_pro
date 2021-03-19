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
        s, f = head, head
        while f and f.next:
            f = f.next.next
            s = s.next
            if s == f:
                break
        if not f or not f.next:
            return None
        h = head
        while h != s:
            h = h.next
            s = s.next
        return h
