class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        """Tree.
        """
        if not root:
            return None
        croot = Node(root.val)
        m = {root: croot}
        nodes = deque([root])
        cnodes = deque([croot])
        while nodes:
            n = nodes.popleft()
            cn = cnodes.popleft()
            for ch in n.children:
                cch = Node(ch.val)
                cn.children.append(cch)
                nodes.append(ch)
                cnodes.append(cch)
        return croot
