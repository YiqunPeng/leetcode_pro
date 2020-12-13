class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        """Hash table.

        Running time: O(a + b) where a == len(A), and b == len(B).
        """
        c = {}
        for b in B:
            cb = collections.Counter(b)
            for k, v in cb.items():
                if k not in c:
                    c[k] = v
                else:
                    c[k] = max(c[k], v)
        res = []
        for a in A:
            ca = collections.Counter(a)
            if all(ca.get(k, 0) >= v for k, v in c.items()):
                res.append(a)
        return res
