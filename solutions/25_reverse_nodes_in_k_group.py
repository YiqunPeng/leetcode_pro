class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        new_head, new_tail = None, None
        while head:
            ohead, otail = head, head
            for i in range(k - 1):
                otail = otail.next
                if not otail:
                    new_tail.next = head
                    return new_head
            head = otail.next
            pre = None
            cur = ohead
            for i in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            if not new_head:
                new_head = pre
            if not new_tail:
                new_tail = ohead
            else:
                new_tail.next = pre
                new_tail = ohead
        return new_head
