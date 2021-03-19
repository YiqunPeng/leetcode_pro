class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast, prev = head, head, None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        a = self.sortList(head)
        b = self.sortList(slow)
        return self._merge(a, b)
    
    def _merge(self, a, b):
        if not a or not b:
            return a or b
        if a.val < b.val:
            a.next = self._merge(a.next, b)
            return a
        else:
            b.next = self._merge(a, b.next)
            return b
