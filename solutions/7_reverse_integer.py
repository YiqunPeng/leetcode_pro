class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            max_int = 2 ** 31
            sign = -1
            x = -x
        else:
            max_int = 2 ** 31 - 1
            sign = 1
        res = 0
        while x != 0:
            r = x % 10
            if max_int // 10 > res or (max_int // 10 == res and max_int % 10 >= r):
                res = res * 10 + r
            else:
                return 0
            x //= 10
        return sign * res
