class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """Binary search.

        Running time: O(logn^2) where n == dividend.
        """
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        dnd, dsr = abs(dividend), abs(divisor)
        res = 0
        while dnd >= dsr:
            x = 1
            d = dsr
            while d + d < dnd:
                d += d
                x += x
            dnd -= d
            res += x
        return res if (dividend >= 0) == (divisor >= 0) else -res
