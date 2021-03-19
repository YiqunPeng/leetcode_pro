class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        res = ListNode()
        p = res
        while head:
            while p.next and head.val > p.next.val:
                p = p.next
            nxt = head.next
            head.next = p.next
            p.next = head
            head = nxt
            if head and head.val < p.next.val:
                p = res
        return res.next
