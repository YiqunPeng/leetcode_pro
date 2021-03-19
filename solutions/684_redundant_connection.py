class Solution:
    
    def __init__(self):
        self.parent = {}

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """Union find.
    
        Running time: O(n) where n is the length of edges.
        """
        for u, v in edges:
            if self._find(v) == self._find(u):
                return [u, v]
            self._union(u, v)
            
    def _find(self, v):
        if v not in self.parent or self.parent[v] == v:
            self.parent[v] = v
        else:
            self.parent[v] = self._find(self.parent[v])
        return self.parent[v]

    def _union(self, u, v):
        self.parent[self._find(u)] = self.parent[v]
