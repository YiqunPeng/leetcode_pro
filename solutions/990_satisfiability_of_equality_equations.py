class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        """Union.

        Running time: O(n) where n is the number of equations.
        """
        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]
        
        def union(x, y):
            f[find(y)] = find(x)
            
            
        f = {}
        
        for e in equations:
            if e[1:3] == '==':
                a, b = e[0], e[3]
                if a not in f:
                    f[a] = a
                if b not in f:
                    f[b] = b
                union(a, b)

        for e in equations:
            if e[1:3] == '!=':
                a, b = e[0], e[3]
                if a == b:
                    return False
                if a in f and b in f and find(a) == find(b):
                    return False
                
        return True
             