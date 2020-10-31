class Solution:
    def maxPower(self, s: str) -> int:
        """String.

        Running time: O(n) where n == len(s).
        """
        res = 1
        c = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                c += 1
            else:
                res = max(res, c)
                c = 1
        return max(res, c)
