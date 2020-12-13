class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """String.

        Running time: O(n) where n = max(len(num1), len(num2)).
        """
        res = []
        c = 0
        p1, p2 = len(num1) - 1, len(num2) - 1
        while p1 >= 0 or p2 >= 0:
            if p1 >= 0 and p2 >= 0:
                c, v = divmod(int(num1[p1]) + int(num2[p2]) + c, 10)
                p1 -= 1
                p2 -= 1
            elif p1 >= 0:
                c, v = divmod(int(num1[p1]) + c, 10)
                p1 -= 1
            else:
                c, v = divmod(int(num2[p2]) + c, 10)
                p2 -= 1
            res.append(str(v))
        if c:
            res.append(str(c))
        return ''.join(res[::-1])
