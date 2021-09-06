class Solution:
    def bulbSwitch(self, n: int) -> int:
        res = 0
        x = 1
        while x * x <= n:
            res += 1
            x += 1
        return res
