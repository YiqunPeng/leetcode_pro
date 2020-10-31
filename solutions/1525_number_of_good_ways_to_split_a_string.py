class Solution:
    def numSplits(self, s: str) -> int:
        """Hash table.

        Running time: O(n) where n == len(s).
        """
        if len(s) < 2:
            return 0
        p = {}
        q = collections.Counter(s)
        res = 0
        for i in range(len(s)):
            p[s[i]] = p.get(s[i], 0) + 1
            q[s[i]] -= 1
            if q[s[i]] == 0:
                q.pop(s[i])
            if len(p) == len(q):
                res += 1
        return res
