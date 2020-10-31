class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
    	"""String.

    	Running time: O(n) where n == len(s).
    	"""
        cur = 0
        seen = {0: -1}
        res = 0
        for i, c in enumerate(s):
            cur ^= 1 << ('aeiou'.find(c) + 1) >> 1
            seen.setdefault(cur, i)
            res = max(res, i - seen[cur])
        return res
