class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        h = head
        while h:
            copy = Node(h.val, h.next)
            h.next = copy
            h = h.next.next
        
        h = head
        while h:
            nxt = h.next
            nxt.random = h.random.next if h.random else None
            h = nxt.next
        
        nhead = head.next
        h = nhead
        while h and h.next:
            h.next = h.next.next
            h = h.next
        
        return nhead
