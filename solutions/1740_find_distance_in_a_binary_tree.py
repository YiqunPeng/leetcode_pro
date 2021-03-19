class Solution:
 
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        lca = self._lca(root, p, q)
        return self._distance(lca, p) + self._distance(lca, q)
        
    def _lca(self, root, p, q):
        if not root or root.val == p or root.val == q:
            return root
        l = self._lca(root.left, p, q)
        r = self._lca(root.right, p, q)
        if l and r:
            return root
        return l if l else r
    
    def _distance(self, root, target):
        if not root:
            return float('inf')
        if root.val == target:
            return 0
        else:
            return 1 + min(self._distance(root.left, target), self._distance(root.right, target))
