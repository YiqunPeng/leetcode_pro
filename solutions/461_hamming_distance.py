class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """Bit manipulation.

        Running time: O(logx).
        """
        res = 0
        
        while x != 0 and y != 0:
            if x % 2 != y % 2:
                res += 1
            x //= 2
            y //= 2
            
        r = x or y
        while r != 0:
            if r % 2:
                res += 1
            r //= 2
        
        return res