# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """Linked list.

        Running Time: O(n) where n is the length of linked list.
        """
        dummy = ListNode(0, head)
        d = dummy
        while dummy.next and dummy.next.next:
            if dummy.next.val == dummy.next.next.val:
                v = dummy.next.val
                while dummy.next and dummy.next.val == v:
                    dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        return d.next
  