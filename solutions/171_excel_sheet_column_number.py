class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        n = len(columnTitle)
        for i in range(n - 1, -1, -1):
            v = ord(columnTitle[i]) - ord('A') + 1
            res = res + 26 ** (n - 1 - i) * v
        return res
