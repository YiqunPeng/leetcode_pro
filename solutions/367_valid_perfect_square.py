class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            m = (l + r) // 2
            v = m * m
            if v == num:
                return True
            elif v < num:
                l = m + 1
            else:
                r = m - 1
        return False
