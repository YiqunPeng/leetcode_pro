class Solution:
    
    def __init__(self):
        self.res = 0
    
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        self._preorder(root, 1)
        return self.res
    
    def _preorder(self, root, seq):
        self.res = max(self.res, seq)
        if root.left:
            if root.left.val == root.val + 1:
                self._preorder(root.left, seq + 1)
            else:
                self._preorder(root.left, 1)
        if root.right:
            if root.right.val == root.val + 1:
                self._preorder(root.right, seq + 1)
            else:
                self._preorder(root.right, 1)
