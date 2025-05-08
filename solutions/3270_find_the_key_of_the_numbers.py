class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        res = 0
        for i in range(4):
            d1, d2, d3 = num1 % 10, num2 % 10, num3 % 10
            num1, num2, num3 = num1 // 10, num2 // 10, num3 // 10
            res = res + min(d1, d2, d3) * 10 ** i
        return res