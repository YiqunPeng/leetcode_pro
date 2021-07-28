class Solution:
    
    def __init__(self):
        self.res = []
    
    def rightSideView(self, root: TreeNode) -> List[int]:
        self._dfs(root, 0)
        return self.res
    
    def _dfs(self, root, depth):
        if not root:
            return
        if len(self.res) == depth:
            self.res.append(root.val)
        self._dfs(root.right, depth + 1)
        self._dfs(root.left, depth + 1)
