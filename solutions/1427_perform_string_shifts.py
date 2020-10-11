class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
    	"""String.

    	Running time: O(n) where n is the length of shift.
    	"""
        rm = 0
        for d, a in shift:
            if d == 0:
                rm -= a
            else:
                rm += a
        rm %= len(shift)
        return s[-rm:] + s[:-rm]
