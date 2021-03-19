class Solution:
    
    def __init__(self):
        self.maxd = 0
    
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self._post_order(root)
        return self.maxd
    
    def _post_order(self, root):
        if not root:
            return 0
        v = sorted([self._post_order(c) for c in root.children], reverse=True)
        if len(v) == 0:
            return 1
        elif len(v) == 1:
            self.maxd = max(self.maxd, v[0])
            return v[0] + 1
        else:
            self.maxd = max(self.maxd, v[0] + v[1])
            return v[0] + 1
