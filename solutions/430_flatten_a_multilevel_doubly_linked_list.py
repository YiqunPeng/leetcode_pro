class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        node = head
        st = []
        while node:
            if node.child:
                if node.next:
                    st.append(node.next)
                node.next = node.child
                node.child.prev = node
                node.child = None
                node = node.next
            elif node.next:
                node = node.next
            elif st:
                n = st.pop()
                node.next = n
                n.prev = node
                node = n
            else:
                node = node.next
        return head
