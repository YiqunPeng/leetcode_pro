class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        n = len(lists)
        if n == 1:
            return lists[0]
        f = self.mergeKLists(lists[:n//2])
        s = self.mergeKLists(lists[n//2:])
        return self._merge(f, s)
    
    def _merge(self, f, s):
        if not f or not s:
            return f or s
        if f.val < s.val:
            f.next = self._merge(f.next, s)
            return f
        else:
            s.next = self._merge(f, s.next)
            return s