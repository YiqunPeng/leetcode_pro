class Solution:
    
    def __init__(self):
        self.parent = {i: i for i in string.ascii_lowercase}
    
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        for i in range(len(A)):
            self._union(A[i], B[i])
        l = list(S)
        for i in range(len(l)):
            l[i] = self._find(l[i])
        return ''.join(l)
    
    def _union(self, a, b):
        pa = self._find(a)
        pb = self._find(b)
        if pa < pb:
            self.parent[pb] = pa
        else:
            self.parent[pa] = pb
            
    def _find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self._find(self.parent[a])
        return self.parent[a]
