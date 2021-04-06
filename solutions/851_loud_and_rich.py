class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(set)
        for x, y in richer:
            graph[x].add(y)
        pquiet = [(i, quiet[i]) for i in range(len(quiet))]
        pquiet.sort(key=lambda x: x[1])
        res = list(range(len(quiet)))
        visited = set()
        for p, q in pquiet:
            visited.add(p)
            self._dfs(p, p, q, graph, res, visited)
        return res
    
    def _dfs(self, p, curr, q, graph, res, visited):
        for nei in graph[curr]:
            if nei not in visited:
                visited.add(nei)
                res[nei] = p
                self._dfs(p, nei, q, graph, res, visited)
