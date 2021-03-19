class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        return self._count(root, distance)[0]
    
    def _count(self, root, distance):
        if not root:
            return 0, {}
        if not root.left and not root.right:
            return 0, {0: 1}
        lc, ld = self._count(root.left, distance)
        rc, rd = self._count(root.right, distance)
        d = defaultdict(int)
        c = lc + rc
        for lk in ld:
            d[lk+1] += ld[lk]
            for i in range(distance - lk - 1):
                c += ld[lk] * rd.get(i, 0)
        for rk in rd:
            d[rk+1] += rd[rk]      
        return c, d
