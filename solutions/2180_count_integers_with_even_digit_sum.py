class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for n in range(1, num + 1):
            if self._cal_digit_sums(n) % 2 == 0:
                res += 1
        return res
        
    def _cal_digit_sums(self, n):
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s