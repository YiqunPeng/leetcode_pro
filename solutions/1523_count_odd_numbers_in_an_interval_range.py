class Solution:
    def countOdds(self, low: int, high: int) -> int:
        c = high - low + 1
        if c % 2 == 1 and low % 2 == 1:
            r = 1
        else:
            r = 0
        return r + c // 2
