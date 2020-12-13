class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Two pointer.

        Running time: O(n) where n is the length of s.
        """
        d = {}
        res = st = 0
        for i, c in enumerate(s):
            if c in d and st <= d[c]:
                st = d[c] + 1
            else:
                res = max(res, i - st + 1)
            d[c] = i
        return res
        