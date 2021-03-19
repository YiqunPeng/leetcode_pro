class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self._is_valid(root.left, float('-inf'), root.val) and self._is_valid(root.right, root.val, float('inf'))
    
    def _is_valid(self, root, minv, maxv):
        if not root:
            return True
        if root.val <= minv or root.val >= maxv:
            return False
        return self._is_valid(root.left, minv, root.val) and self._is_valid(root.right, root.val, maxv)
