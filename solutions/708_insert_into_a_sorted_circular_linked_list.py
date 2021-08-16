class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        """Linked list.

        Running time: O(n) where n is the number of nodes in the list.
        """
        node = Node(insertVal)
        if not head:
            node.next = node
            return node
        h = head
        while h.next != head and h.next.val >= h.val:
            h = h.next
        if h.next.val >= node.val or node.val >= h.val:
            node.next = h.next
            h.next = node
            return head
        while h.next.val < node.val:
            h = h.next
        node.next = h.next
        h.next = node
        return head
    