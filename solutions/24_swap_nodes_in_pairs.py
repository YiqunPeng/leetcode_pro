class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        node = dummy
        while dummy.next and dummy.next.next:
            a, b = dummy.next, dummy.next.next
            a.next = b.next
            b.next = a
            dummy.next = b
            dummy = a
        return node.next
