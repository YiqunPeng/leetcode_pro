class Solution:
    def titleToNumber(self, s: str) -> int:
    	"""Math.

    	Running time: O(n) where n is the length of s.
    	"""
        n = len(s)
        
        ret = 0
        
        for i, c in enumerate(s):
            ret += (ord(c) - ord('A') + 1) * 26 ** (n - i - 1)
        
        return ret