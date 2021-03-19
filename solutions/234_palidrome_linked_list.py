class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        m = self._find_middle(head)
        t = self._reverse(m.next)
        return self._compare(head, t)
    
    def _find_middle(self, head):
        s, f = head, head
        while f and f.next and f.next.next:
            s = s.next
            f = f.next.next
        return s
    
    def _reverse(self, head):
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
    
    def _compare(self, a, b):
        while b:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next
        return True
