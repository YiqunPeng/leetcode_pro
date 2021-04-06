class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        """DFS.
        """
        graph = defaultdict(set)
        for a, b in allowedSwaps:
            graph[a].add(b)
            graph[b].add(a)
        visited = set()
        res = 0
        for i in range(len(source)):
            if i not in visited:
                visited.add(i)
                s, t = defaultdict(int), defaultdict(int)
                self._dfs(s, t, graph, i, visited, source, target)
                for k in s:
                    res += max(0, s[k] - t[k])
        return res
    
    def _dfs(self, s, t, graph, i, visited, source, target):
        s[source[i]] += 1
        t[target[i]] += 1
        for nei in graph[i]:
            if nei not in visited:
                visited.add(nei)
                self._dfs(s, t, graph, nei, visited, source, target)
