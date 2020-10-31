class Solution:
    def customSortString(self, S: str, T: str) -> str:
        """Hash table.

        Running time: O(s + t) where s == len(S) and t == len(T).
        """
        c = collections.Counter(T)
        res = ''
        for s in S:
            if s in c:
                res = res + s * c[s]
                c[s] = 0
        for k, v in c.items():
            res = res + k * v
        return res
