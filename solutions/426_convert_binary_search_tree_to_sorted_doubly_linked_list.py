class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        lmin, rmax = self._postorder(root)
        lmin.left = rmax
        rmax.right = lmin
        return lmin
    
    def _postorder(self, root):
        if not root:
            return None, None
        if not root.left and not root.right:
            return root, root
        lmin, lmax = self._postorder(root.left)
        rmin, rmax = self._postorder(root.right)
        min_node, max_node = root, root
        if lmin:
            lmax.right = root
            root.left = lmax
            min_node = lmin
        if rmax:
            rmin.left = root
            root.right = rmin
            max_node = rmax
        return min_node, max_node
