class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = [root.val]
        s = set([root])
        lb = []
        self._get_left_boundary(root.left, lb)
        for node in lb:
            if node not in s:
                s.add(node)
                res.append(node.val)
        leaves = []
        self._get_leaves(root, leaves)
        for leaf in leaves:
            if leaf not in s:
                s.add(leaf)
                res.append(leaf.val)
        rb = []
        self._get_right_boundary(root.right, rb)
        for node in rb[::-1]:
            if node not in s:
                s.add(node)
                res.append(node.val)
        return res
    
    def _get_left_boundary(self, root, lb):
        if not root:
            return
        lb.append(root)
        if root.left:
            self._get_left_boundary(root.left, lb)
        elif root.right:
            self._get_left_boundary(root.right, lb)
    
    def _get_right_boundary(self, root, rb):
        if not root:
            return
        rb.append(root)
        if root.right:
            self._get_right_boundary(root.right, rb)
        elif root.left:
            self._get_right_boundary(root.left, rb)
            
    def _get_leaves(self, root, leaves):
        if not root:
            return
        if not root.left and not root.right:
            leaves.append(root)
            return
        self._get_leaves(root.left, leaves)
        self._get_leaves(root.right, leaves)
