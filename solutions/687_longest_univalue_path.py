class Solution:
    
    def __init__(self):
        self.res = 0
    
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return self.res
        self._postorder(root)
        return self.res
    
    def _postorder(self, root):
        if not root:
            return -1
        lcnt = self._postorder(root.left)
        rcnt = self._postorder(root.right)
        if root.left and root.right and root.val == root.left.val == root.right.val:
            self.res = max(self.res, lcnt + rcnt + 2)
            return max(lcnt, rcnt) + 1
        elif root.left and root.left.val == root.val:
            self.res = max(self.res, lcnt + 1)
            return lcnt + 1
        elif root.right and root.right.val == root.val:
            self.res = max(self.res, rcnt + 1)
            return rcnt + 1
        return 0
