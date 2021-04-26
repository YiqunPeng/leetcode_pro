class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
        if len(graph[destination]) > 0:
            return False
        cpath = [0] * n
        cpath[source] = 1
        return self._dfs(graph, source, destination, cpath)
    
    def _dfs(self, graph, node, dest, cpath):
        if not graph[node]:
            return dest == node
        if cpath[node] == 2:
            return True
        for nxt in graph[node]:
            if cpath[nxt] == 1:
                return False
            cpath[nxt] = 1
            if not self._dfs(graph, nxt, dest, cpath):
                return False
            cpath[nxt] = 0
        cpath[node] = 2
        return True
