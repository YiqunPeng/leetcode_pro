class Solution:
    
    def __init__(self):
        self.visited = []
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.visited = [0] * len(graph)
        for i in range(len(graph)):
            if self.visited[i] == 0:
                self._dfs(graph, i)
        return [i for i in range(len(graph)) if self.visited[i] != -1]
    
    def _dfs(self, graph, i):
        if self.visited[i] != 0:
            return self.visited[i] == 1
        self.visited[i] = -1
        for nei in graph[i]:
            if not self._dfs(graph, nei):
                return False
        self.visited[i] = 1
        return True
