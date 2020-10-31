class Solution:
    def firstUniqChar(self, s: str) -> int:
    	"""String.

    	Running time: O(n) where n == len(s).
    	"""
        c = collections.Counter(s)
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        return -1
