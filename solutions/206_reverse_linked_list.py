class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """Recursive.

        Running time: O(n) where n is the length of the list.
        """
        def reverse(node):
            if not node.next:
                return node, node         
            nhead, ntail = reverse(node.next)
            ntail.next = node
            return nhead, node
        
        if not head:
            return None     
        nhead, ntail = reverse(head)
        ntail.next = None
        return nhead

    def reverseList_iterative(self, head: ListNode) -> ListNode:
        """Iterative.

        Running time: O(n) where n is the length of the list.
        """
        pre = None
        cur = head
        
        while cur:
            n = cur.next
            cur.next = pre
            pre = cur
            cur = n

        return pre
