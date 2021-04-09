class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """Topological sort.
        """
        if n == 1:
            return [0]
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        leaves = deque()
        for k in graph:
            if len(graph[k]) == 1:
                leaves.append(k)
        while n > 2:
            n -= len(leaves)
            nleaves = []
            for node in leaves:
                for nei in graph[node]:
                    graph[nei].remove(node)
                    if len(graph[nei]) == 1:
                        nleaves.append(nei)
            leaves = nleaves
        return leaves
