class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
    	"""String.

    	Running time: O(h * n) where h == len(haystack) and n == len(needle).
    	"""
        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
