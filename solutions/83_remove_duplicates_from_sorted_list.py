# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
    	"""Linked list

    	Running Time: O(n) where n is the length of the list.
    	"""
        h = head
        while h and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return h
 