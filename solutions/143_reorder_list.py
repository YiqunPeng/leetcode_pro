class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        m = self._find_middle(head)
        n = m.next
        m.next = None
        t = self._reverse(n)
        return self._merge(head, t)
    
    def _find_middle(self, head):
        s, f = head, head
        while f and f.next and f.next.next:
            s = s.next
            f = f.next.next
        return s
    
    def _reverse(self, head):
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev
    
    def _merge(self, a, b):
        n = a
        while b:
            anxt = n.next
            bnxt = b.next
            b.next = n.next
            n.next = b
            b = bnxt
            n = anxt
        return a
