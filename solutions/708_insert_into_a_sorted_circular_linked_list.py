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
            nhead = Node(insertVal)
            nhead.next = nhead
            return nhead
        h = head
        while h.next != head and h.val <= h.next.val:
            h = h.next
        max_node = h
        min_node = h.next
        if max_node.val == min_node.val or insertVal >= max_node.val or insertVal <= min_node.val:
            new_node = Node(insertVal, min_node)
            max_node.next = new_node
            return head
        node = min_node
        while node.next != min_node:
            if node.next.val >= insertVal:
                new_node = Node(insertVal, node.next)
                node.next = new_node
                return head
            node = node.next
    