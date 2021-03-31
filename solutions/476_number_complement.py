class Solution:
    def findComplement(self, num: int) -> int:
        b = []
        while num != 0:
            b.append(1 - num % 2)
            num //= 2
        res = 0
        for i in range(len(b)):
            res += b[i] * 2 ** i
        return res
