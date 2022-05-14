class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self._postorder(root)[2]
    
    def _postorder(self, root):
        if not root:
            return 0, 0, 0
        ls, ln, lr = self._postorder(root.left)
        rs, rn, rr = self._postorder(root.right)
        r = lr + rr
        if (root.val + ls + rs) // (ln + rn + 1) == root.val:
            r += 1
        return ls + rs + root.val, ln + rn + 1, r
