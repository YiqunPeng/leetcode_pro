class Solution:
    
    def __init__(self):
        self.res = 0
    
    def longestConsecutive(self, root: TreeNode) -> int:
        self._postorder(root)
        return self.res
    
    def _postorder(self, root):
        if not root:
            return 0, 0
        li, ld = self._postorder(root.left)
        ri, rd = self._postorder(root.right)
        ni, nd = 1, 1
        if root.left and root.left.val == root.val - 1:
            nd += ld
        if root.right and root.right.val == root.val - 1:
            nd = max(nd, 1 + rd)
        if root.left and root.left.val == root.val + 1:
            ni += li
        if root.right and root.right.val == root.val + 1:
            ni = max(ni, 1 + ri)
        if root.left and root.right:
            if root.left.val - 1 == root.val == root.right.val + 1:
                self.res = max(self.res, li + rd + 1)
            if root.left.val + 1 == root.val == root.right.val - 1:
                self.res = max(self.res, ld + ri + 1)
        self.res = max(self.res, ni, nd)
        return ni, nd
