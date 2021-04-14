class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = self._add(num)
        return num
    
    def _add(self, num):
        res = 0
        while num != 0:
            res += num % 10
            num //= 10
        return res
