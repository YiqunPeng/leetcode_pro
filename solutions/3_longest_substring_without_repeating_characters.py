class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Two pointer.

        Running time: O(n) where n is the length of s.
        """
        d = dict()
        res = 0
        i = 0
        for j, c in enumerate(s):
            if c in d and i <= d[c]:
                i = d[c] + 1
            res = max(res, j - i + 1)
            d[c] = j
        return res
        