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
        p = head
        
        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        
        return head
 