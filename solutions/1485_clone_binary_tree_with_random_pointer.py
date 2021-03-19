class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if not root:
            return None
        croot = NodeCopy(root.val)
        node_d = {None: None, root: croot}
        q = deque([root])
        cq = deque([croot])
        while q:
            node = q.popleft()
            cnode = cq.popleft()
            if node.left:
                cleft = NodeCopy(node.left.val)
                cnode.left = cleft
                q.append(node.left)
                cq.append(cleft)
                node_d[node.left] = cleft
            if node.right:
                cright = NodeCopy(node.right.val)
                cnode.right = cright
                q.append(node.right)
                cq.append(cright)
                node_d[node.right] = cright
        q = deque([root])
        cq = deque([croot])
        while q:
            node = q.popleft()
            cnode = cq.popleft()
            cnode.random = node_d[node.random]
            if node.left:
                q.append(node.left)
                cq.append(cnode.left)
            if node.right:
                q.append(node.right)
                cq.append(cnode.right)
        return croot
