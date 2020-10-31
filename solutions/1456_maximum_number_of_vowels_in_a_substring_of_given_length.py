class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """Sliding window.

        Running time: O(n) where n == len(s).
        """
        res = 0
        c = 0
        v = set(['a', 'e', 'i', 'o', 'u'])
        for i in range(k - 1):
            if s[i] in v:
                c += 1
        for i in range(k - 1, len(s)):
            if s[i] in v:
                c += 1
            res = max(res, c)
            if s[i - k + 1] in v:
                c -= 1
        return res
