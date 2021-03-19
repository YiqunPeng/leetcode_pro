class Solution:
    
    def __init__(self):
        self.maxd = 0
        self.tree = defaultdict(set)
    
    def treeDiameter(self, edges: List[List[int]]) -> int:
        for u, v in edges:
            self.tree[u].add(v)
        self._traverse(0)
        return self.maxd
        
    def _traverse(self, node):
        v = sorted([self._traverse(n) for n in self.tree[node]], reverse=True)
        if len(v) == 0:
            return 1
        elif len(v) == 1:
            self.maxd = max(self.maxd, v[0])
        else:
            self.maxd = max(self.maxd, v[0] + v[1])
        return v[0] + 1
