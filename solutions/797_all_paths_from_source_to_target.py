class Solution:
    
    def __init__(self):
        self.res = []
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self._dfs(graph, 0, [0])
        return self.res
    
    def _dfs(self, graph, node, path):
        if node == len(graph) - 1:
            self.res.append(path)
            return
        for nei in graph[node]:
            self._dfs(graph, nei, path + [nei])
