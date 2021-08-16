class Solution:
    
    def __init__(self):
        self.res = 0
    
    def diameter(self, root: 'Node') -> int:
        self._dfs(root)
        return self.res
    
    def _dfs(self, root):
        if not root:
            return 0
        f, s = 0, 0
        for c in root.children:
            v = self._dfs(c)
            if v >= f:
                f, s = v, f
            elif v >= s:
                s = v
        self.res = max(self.res, f + s)
        return f + 1
