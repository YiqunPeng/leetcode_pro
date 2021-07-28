class Solution:
    
    def __init__(self):
        self.res = 0
    
    def longestConsecutive(self, root: TreeNode) -> int:
        self._dfs(root)
        return self.res
    
    def _dfs(self, root):
        if not root:
            return 0
        lseq = self._dfs(root.left)
        rseq = self._dfs(root.right)
        seq = 1
        if root.left and root.val == root.left.val - 1:
            seq = max(seq, lseq + 1)
        if root.right and root.val == root.right.val - 1:
            seq = max(seq, rseq + 1)
        self.res = max(self.res, seq)
        return seq
