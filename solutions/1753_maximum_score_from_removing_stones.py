class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        res = 0
        values = sorted([a, b, c])
        while values[1] != 0:
            values[1] -= 1
            values[2] -= 1
            res += 1
            values.sort()
        return res
