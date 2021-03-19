class Solution:
    def reverseList(self, head: ListNode, pre=None) -> ListNode:
        """Recursive.

        Running time: O(n) where n is the length of the list.
        """
        if not head:
            return pre
        nxt = head.next
        head.next = pre
        return self.reverseList(nxt, head)

    def reverseList_iterative(self, head: ListNode) -> ListNode:
        """Iterative.

        Running time: O(n) where n is the length of the list.
        """
        pre = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        return pre
