class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """DFS.

        Running time: O(e + q * n) where e is the number of equations, 
                      q is the number of queries,
                      n is the number of nodes in the graph.
        """
        def dfs(s, e, val, visited):
            if not graph[s]:
                return -1.0
            if s == e:
                return val
            for n in graph[s]:
                if n not in visited:
                    visited.add(n)
                    res = dfs(n, e, val * evals[(s, n)], visited)
                    if res != -1.0:
                        return res
                    visited.remove(n)
            return -1.0
            
        
        graph = collections.defaultdict(set)
        evals = {}
        for i in range(len(equations)):
            A, B, k = equations[i][0], equations[i][1], values[i]
            graph[A].add(B)
            graph[B].add(A)
            evals[(A, B)] = k
            evals[(B, A)] = 1.0 / k

        return [dfs(a, b, 1.0, set([a])) for a, b in queries]
            