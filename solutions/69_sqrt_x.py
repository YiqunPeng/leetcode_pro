class Solution:
    def mySqrt(self, x: int) -> int:
        """Binary Search

        Running Time: O(log x)
        """
        l, r = 0, x // 2 + 1
        while l <= r:
            m = l + (r - l) // 2
            if m * m <= x and (m + 1) * (m + 1) > x:
                return m
            elif m * m < x:
                l = m + 1
            else:
                r = m - 1
                
        return r
