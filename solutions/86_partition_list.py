class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        s = ListNode()
        c = s
        dummy = ListNode(0, head)
        d = dummy
        while dummy and dummy.next:
            if dummy.next.val < x:
                c.next = dummy.next
                dummy.next = dummy.next.next
                c = c.next
            else: 
                dummy = dummy.next
        c.next = d.next
        return s.next
