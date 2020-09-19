class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """Binary search.

        Running time: O(logdividend).
        """
        s = 1
        if dividend < 0:
            s = 0 - s
            dividend = 0 - dividend
        if divisor < 0:
            s = 0 - s
            divisor = 0 - divisor
            
        res = 0
        
        while dividend >= divisor:
            d = divisor
            q = 1
            while d + d < dividend:
                d = d + d
                q = q + q
            res += q
            dividend -= d
        
        res = res if s > 0 else 0 - res
        if res < - 2 ** 31 or res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return res