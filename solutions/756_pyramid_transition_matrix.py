class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        d = defaultdict(set)
        for a in allowed:
            d[a[:2]].add(a[2])
        return self._dfs(bottom, d, 0, "")
    
    def _dfs(self, bottom, d, p, nxt):
        if len(bottom) == 1:
            return True
        if p == len(bottom) - 1:
            return self._dfs(nxt, d, 0, "")
        for i in d[bottom[p:p+2]]:
            if self._dfs(bottom, d, p+1, nxt+i):
                return True
        return False
