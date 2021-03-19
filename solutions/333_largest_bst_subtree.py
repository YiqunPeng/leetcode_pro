class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        return self._post_order(root)[0]
        
    def _post_order(self, root):
        if not root:
            return 0, True, None, None
        if not root.left and not root.right:
            return 1, True, root.val, root.val
        ln, lbst, lmin, lmax = self._post_order(root.left)
        rn, rbst, rmin, rmax = self._post_order(root.right)
        if not lbst or not rbst or (lmax and root.val <= lmax) or (rmin and root.val >= rmin):
            return max(ln, rn), False, None, None
        return ln + rn + 1, True, lmin if lmin else root.val, rmax if rmax else root.val
