class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        v = self._traverse(head)
        if v:
            nhead = ListNode(1, head)
            return nhead
        else:
            return head
    
    def _traverse(self, head):
        if not head:
            return 1
        head.val += self._traverse(head.next)
        if head.val > 9:
            head.val -= 10
            return 1
        return 0
