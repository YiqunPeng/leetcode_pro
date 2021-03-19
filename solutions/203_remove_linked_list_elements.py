# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        d = dummy
        while d and d.next:
            if d.next.val == val:
                d.next = d.next.next
            else:
                d = d.next
        return dummy.next
