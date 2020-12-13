class Solution:
    def balancedString(self, s: str) -> int:
        """String.

        Running time: O(n) where n == len(s).
        """
        c = collections.Counter(s)
        n = res = len(s)
        i = 0
        for j in range(n):
            c[s[j]] -= 1
            while i < n and all(c[k] <= n / 4 for k in 'QWER'):
                res = min(res, j - i + 1)
                c[s[i]] += 1
                i += 1
        return res
