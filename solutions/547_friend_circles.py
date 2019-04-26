class Solution:    
    def findCircleNum(self, M: List[List[int]]) -> int:
        """Union Find

        Running time: O(n^3) as UF is O(n) in worst case.
        """
        n = len(M)
        if n == 0: 
            return 0
        
        p = {i: i for i in range(n)}
        
        def find(x : int) -> int:
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        def union(x : int, y : int) -> None:
            p[find(x)] = find(y)
                    
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1:
                    union(i, j)
                   
        return len([k for k, v in p.items() if k == v])
