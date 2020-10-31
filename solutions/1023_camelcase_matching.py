class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        """String.
        """
        n = len(queries)
        p = [0] * n
        res = self._same_upper(queries, pattern)        
        for c in pattern:
            for i, q in enumerate(queries):
                while p[i] < len(q) and q[p[i]] != c:
                    p[i] += 1
                if p[i] == len(q):
                    res[i] = False
                else:
                    p[i] += 1
        return res
    
    def _same_upper(self, qs, p):
        res = []
        pu = [i for i in p if 'A' <= i <= 'Z']
        for q in qs:
            qu = [i for i in q if 'A' <= i <= 'Z']
            if pu == qu:
                res.append(True)
            else:
                res.append(False)
        return res
