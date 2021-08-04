# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = h = ListNode()
        c = 0
        while l1 or l2 or c:
            if l1 and l2:
                c, v = divmod(l1.val + l2.val + c, 10)
                l1 = l1.next
                l2 = l2.next
            elif l1:
                c, v = divmod(l1.val + c, 10)
                l1 = l1.next
            elif l2:
                c, v = divmod(l2.val + c, 10)
                l2 = l2.next
            else:
                v, c = c, 0
            node = ListNode(v)
            h.next = node
            h = h.next
        return head.next
