class Solution:
    def countSegments(self, s: str) -> int:
    	"""String.

    	Running time: O(n) where n == len(s).
    	"""
        p = s.split(' ')
        res = 0
        for i in p:
            if i:
                res += 1
        return res
