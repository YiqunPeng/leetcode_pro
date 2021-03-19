class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0, head)
        d = dummy
        for i in range(left - 1):
            d = d.next
        start = d
        for i in range(right - left + 2):
            d = d.next
        end = d
        prev = end
        cur = start.next
        for i in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        start.next = prev
        return dummy.next
