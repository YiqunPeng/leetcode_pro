class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
    	"""String.

    	Running time: O(n^2) where n == len(s).
    	"""
        t = s + s
        return s in t[1:-1]
