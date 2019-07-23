class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """Union find.
    
        Running time: O(n) where n is the length of edges.
        """
        def find(v):
            if f[v] != v:
                f[v] = find(f[v])
            return f[v]
        
        def union(v1, v2):
            f[find(v1)] = find(v2)
        
        N = len(edges)
        f = [i for i in range(1 + N)]
        
        for u, v in edges:
            if find(u) == find(v):
                return [u, v]
            else:
                union(u, v)