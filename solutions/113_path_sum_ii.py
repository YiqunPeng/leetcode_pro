class Solution:
    
    def __init__(self):
        self.res = []
    
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self._dfs(root, targetSum, [])
        return self.res
    
    def _dfs(self, root, t, path):
        if not root:
            return
        if not root.left and not root.right:
            if t == root.val:
                self.res.append(path + [root.val])
            return 
        self._dfs(root.left, t - root.val, path + [root.val])
        self._dfs(root.right, t - root.val, path + [root.val])
