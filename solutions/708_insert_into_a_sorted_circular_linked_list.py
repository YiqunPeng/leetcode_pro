"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        """Linked list.

        Running time: O(n) where n is the number of nodes in the list.
        """
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        n = head
        if n.val > n.next.val:
            g = n
        else:
            n = n.next
            while n != head and n.val <= n.next.val:
                n = n.next
            g = n
        if insertVal >= g.val or insertVal <= g.next.val:
            node = Node(insertVal, g.next)
            g.next = node
            return head
        while not (g.val <= insertVal <= g.next.val):
            g = g.next
        node = Node(insertVal, g.next)
        g.next = node
        return head
    