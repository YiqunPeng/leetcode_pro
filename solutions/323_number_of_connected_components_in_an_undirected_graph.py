class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        seen = set()
        res = 0
        for i in range(n):
            if i not in seen:
                seen.add(i)
                res += 1
                self._dfs(i, seen, g)
        return res
    
    def _dfs(self, i, seen, g):
        for j in g[i]:
            if j not in seen:
                seen.add(j)
                self._dfs(j, seen, g)
