class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        p, q = dummy, dummy
        for i in range(n + 1):
            p = p.next
        while p:
            p = p.next
            q = q.next
        q.next = q.next.next
        return dummy.next
