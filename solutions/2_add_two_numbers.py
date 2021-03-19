# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        h = head
        c = 0
        while l1 or l2:
            if l1 and l2:
                v = l1.val + l2.val + c
                l1 = l1.next
                l2 = l2.next
            elif l1:
                v = l1.val + c
                l1 = l1.next
            else:
                v = l2.val + c
                l2 = l2.next
            node = ListNode(v % 10)
            c = v // 10
            h.next = node
            h = node
        if c:
            node = ListNode(1)
            h.next = node
        return head.next
   