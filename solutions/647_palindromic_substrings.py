class Solution:
    def countSubstrings(self, s: str) -> int:
        """DP.

        Running time: O(n^2) where n == len(s).
        """
        p = set()
        n = len(s)
        res = n
        for i in range(n):
            for j in range(0, i):
                if s[j] == s[i] and (i - 1 <= j + 1 or (j + 1, i - 1) in p):
                    res += 1
                    p.add((j, i))
        return res
