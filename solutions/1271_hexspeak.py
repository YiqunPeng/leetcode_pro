class Solution:
    def toHexspeak(self, num: str) -> str:
        """String.
        """
        res = ''
        d = {0: 'O', 1: 'I', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        num = int(num)
        while num > 0:
            r = num % 16
            if r not in d:
                return 'ERROR'
            else:
                res += d[r]
            num //= 16
        return res[::-1]
