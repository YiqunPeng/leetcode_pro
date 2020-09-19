class Solution:
    def reverse(self, x: int) -> int:
    	"""Math.

    	Running time: O(logx).
    	"""
        s = 1 if x >= 0 else -1
        
        r = 0
        x = abs(x)
        while x != 0:
            r = r * 10 + x % 10
            x //= 10
        
        return s * r if -2 ** 31 <= s * r <= 2 ** 31 - 1 else 0