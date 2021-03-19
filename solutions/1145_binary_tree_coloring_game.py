class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        xnode = self._find_x(root, x)
        lcnt = self._count(xnode.left)
        rcnt = self._count(xnode.right)
        return max(lcnt, rcnt, n - lcnt - rcnt - 1) > n / 2
    
    def _find_x(self, root, x):
        if not root or root.val == x:
            return root
        return self._find_x(root.left, x) or self._find_x(root.right, x)
    
    def _count(self, root):
        if not root:
            return 0
        return 1 + self._count(root.left) + self._count(root.right)
