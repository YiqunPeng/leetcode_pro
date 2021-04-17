class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            r = (columnNumber - 1) % 26
            res.append(chr(ord('A') + r))
            columnNumber = (columnNumber - 1) // 26
        return ''.join(res[::-1])
