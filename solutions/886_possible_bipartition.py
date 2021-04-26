class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for a, b in dislikes:
            graph[a].add(b)
            graph[b].add(a)
        marks = {}
        for i in range(1, N + 1):
            if i not in marks:
                marks[i] = 0
                if not self._dfs(i, 0, marks, graph):
                    return False
        return True
    
    def _dfs(self, node, m, marks, graph):
        for nei in graph[node]:
            if nei in marks:
                if marks[nei] == m:
                    return False
            else:
                marks[nei] = 1 - m
                if not self._dfs(nei, 1 - m, marks, graph):
                    return False
        return True
