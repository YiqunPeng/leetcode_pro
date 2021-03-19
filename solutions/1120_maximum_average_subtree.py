class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        return self._max_avg(root, 0)[2]
    
    def _max_avg(self, root, max_avg):
        if not root:
            return 0, 0, max_avg
        lsum, lcnt, lmax_avg = self._max_avg(root.left, max_avg)
        rsum, rcnt, rmax_avg = self._max_avg(root.right, max_avg)
        s = lsum + rsum + root.val
        c = lcnt + rcnt + 1
        max_avg = max(lmax_avg, rmax_avg, s / c)
        return s, c, max_avg
