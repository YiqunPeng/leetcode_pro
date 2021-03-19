class Solution:
     def maxAncestorDiff(self, root: TreeNode) -> int:
        return self._traverse(root, root.val, root.val)
    
    def _traverse(self, root, minv, maxv):
        if not root:
            return maxv - minv
        minv = min(minv, root.val)
        maxv = max(maxv, root.val)
        l = self._traverse(root.left, minv, maxv)
        r = self._traverse(root.right, minv, maxv)
        return max(l, r)
