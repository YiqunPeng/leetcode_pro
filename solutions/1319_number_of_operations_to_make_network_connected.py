class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n > len(connections) + 1:
            return -1
        seen = [0] * n
        g = self._build_graph(connections)
        sub = 0
        for i in range(n):
            if not seen[i]:
                seen[i] = 1
                sub += 1
                self._dfs(g, i, seen)
        return sub - 1
    
    def _build_graph(self, connections):
        g = defaultdict(set)
        for a, b in connections:
            g[a].add(b)
            g[b].add(a)
        return g
    
    def _dfs(self, g, i, seen):
        for nxt in g[i]:
            if not seen[nxt]:
                seen[nxt] = 1
                self._dfs(g, nxt, seen)
