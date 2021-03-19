class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n
        for i in range(n):
            if color[i] == 0 and len(graph[i]) > 0:
                color[i] = 1
                q = deque([i])
                while q:
                    for i in range(len(q)):
                        node = q.popleft()
                        for nei in graph[node]:
                            if color[nei] == 0:
                                q.append(nei)
                                color[nei] = -color[node]
                            elif color[nei] == color[node]:
                                return False
        return True
