class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    	"""Hash table.

    	Running time: O(n) where n == len(s).
    	"""
        d = {}
        res = 0
        for i, c in enumerate(s):
            if c in d:
                res = max(res, i - d[c] - 1)
            else:
                d[c] = i
        return res if len(d) != len(s) else -1
