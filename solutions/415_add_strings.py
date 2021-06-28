class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """String.

        Running time: O(n) where n = max(len(num1), len(num2)).
        """
        res = []
        p1, p2 = len(num1) - 1, len(num2) - 1
        c = 0
        while p1 >= 0 or p2 >= 0:
            if p1 >= 0 and p2 >= 0:
                c, v = divmod(ord(num1[p1]) - ord('0') + ord(num2[p2]) - ord('0') + c, 10)
                p1, p2 = p1 - 1, p2 - 1
            elif p1 >= 0:
                c, v = divmod(ord(num1[p1]) - ord('0') + c, 10)
                p1 -= 1
            else:
                c, v = divmod(ord(num2[p2]) - ord('0') + c, 10)
                p2 -= 1
            res.append(str(v))
        if c == 1:
            res.append('1')
        return ''.join(res[::-1])
