class Solution:
    def convertToTitle(self, n: int) -> str:
    	"""Recursive.

    	Running time: O(logn).
    	"""
        def convert(m):
            if not m:
                return ''
            return convert((m - 1) // 26) + chr(ord('A') + (m - 1) % 26)
    
        return convert(n)