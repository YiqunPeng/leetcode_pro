class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x // 2 + 1
        while l <= r:
            m = (l + r) // 2
            if m ** 2 <= x and (m + 1) ** 2 > x:
                return m
            elif m ** 2 > x:
                r = m - 1
            else:
                l = m + 1
