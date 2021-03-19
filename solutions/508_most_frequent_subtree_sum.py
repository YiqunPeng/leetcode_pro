class Solution:
    
    def __init__(self):
        self.f = defaultdict(int)
    
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self._post_order(root)
        res = []
        maxf = 0
        for k, v in self.f.items():
            if v > maxf:
                maxf = v
                res = [k]
            elif v == maxf:
                res.append(k)
        return res
    
    def _post_order(self, root):
        if not root:
            return 0
        l = self._post_order(root.left)
        r = self._post_order(root.right)
        v = l + r + root.val
        self.f[v] += 1
        return v
