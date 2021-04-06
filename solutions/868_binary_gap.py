class Solution:
    def binaryGap(self, n: int) -> int:
        res = 0
        pre = None
        p = 0
        while n != 0:
            r = n % 2
            n //= 2
            if r == 1 and pre is not None:
                res = max(res, p - pre)
                pre = p
            elif r == 1:
                pre = p
            p += 1
        return res
