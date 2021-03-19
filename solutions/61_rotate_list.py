# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """Linked list

        Running Time: O(n) where n is the length of linked list.
        """
        if not head:
            return None
        n = head
        l = 0
        while n:
            l += 1
            n = n.next
        k = k % l
        if k == 0:
            return head
        ot, nt = head, head
        for i in range(k):
            ot = ot.next
        while ot.next:
            ot = ot.next
            nt = nt.next
        nh = nt.next
        nt.next = None
        ot.next = head
        return nh
        