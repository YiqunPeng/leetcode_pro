class Solution:
    def totalMoney(self, n: int) -> int:
        d, m = divmod(n, 7)
        return (49 + 7 * d) * d // 2 + (2 * d + m + 1) * m // 2
