class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        rmin, rmax = self._traverse(root)
        rmin.left = rmax
        rmax.right = rmin
        return rmin
    
    def _traverse(self, root):
        if not root:
            return None, None
        lmin, lmax = self._traverse(root.left)
        rmin, rmax = self._traverse(root.right)
        if not root.left and not root.right:
            return root, root
        if not root.left:
            root.right = rmin
            rmin.left = root
            return root, rmax
        if not root.right:
            root.left = lmax
            lmax.right = root
            return lmin, root
        root.left = lmax
        lmax.right = root
        root.right = rmin
        rmin.left = root
        return lmin, rmax
