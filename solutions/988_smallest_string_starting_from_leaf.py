class Solution:
    
    def __init__(self):
        self.small = None
    
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self._dfs(root, [])
        return self.small
        
    def _dfs(self, root, path):
        if not root:
            return 
        if not root.left and not root.right:
            path += [chr(ord('a') + root.val)]
            s = ''.join(path[::-1])
            if not self.small or self.small > s:
                self.small = s
            return
        if root.left:
            self._dfs(root.left, path + [chr(ord('a') + root.val)])
        if root.right:
            self._dfs(root.right, path + [chr(ord('a') + root.val)])
