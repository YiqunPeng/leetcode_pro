class Solution:
    def connect(self, root: 'Node') -> 'Node':
        oroot = root
        nxt_dummy = Node()
        p = nxt_dummy
        while root:
            if root.left:
                p.next = root.left
                p = p.next
            if root.right:
                p.next = root.right
                p = p.next
            if root.next:
                root = root.next
            else:
                root = nxt_dummy.next
                nxt_dummy = Node()
                p = nxt_dummy
        return oroot
