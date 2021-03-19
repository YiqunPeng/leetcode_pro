class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self._post_order(root)[1]
    
    def _post_order(self, root):
        if not root:
            return 0, None
        ld, ln = self._post_order(root.left)
        rd, rn = self._post_order(root.right)
        if ld > rd:
            return ld + 1, ln
        elif ld < rd:
            return rd + 1, rn
        else:
            return ld + 1, root
