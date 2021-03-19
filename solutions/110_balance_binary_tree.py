class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self._helper(root)[1]
    
    def _helper(self, root):
        if not root:
            return 0, True
        lh, lb = self._helper(root.left)
        rh, rb = self._helper(root.right)
        if not lb or not rb or abs(lh - rh) > 1:
            return max(lh, rh) + 1, False
        return max(lh, rh) + 1, True
