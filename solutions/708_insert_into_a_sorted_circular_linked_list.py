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
        insertNode = Node(insertVal)
        
        if not head:
            insertNode.next = insertNode
            return insertNode
        
        p_head = head
        while p_head.next != head and p_head.val <= p_head.next.val:
            p_head = p_head.next
        
        if insertVal > p_head.val or insertVal < p_head.next.val:
            insertNode.next = p_head.next
            p_head.next = insertNode
            return head
    
        s_node = p_head.next       
        p_s_node = s_node
        while p_s_node.next != s_node and p_s_node.next.val < insertVal:
            p_s_node = p_s_node.next
        
        insertNode.next = p_s_node.next
        p_s_node.next = insertNode
        
        return head
    