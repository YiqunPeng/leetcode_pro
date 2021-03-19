class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node = head
        while node:
            c = Node(node.val, node.next, node.random)
            node.next = c
            node = c.next
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
        dummy = Node(0)
        cur = dummy
        node = head
        while node:
            cur.next = node.next
            node.next = node.next.next
            node = node.next
            cur = cur.next
        return dummy.next
