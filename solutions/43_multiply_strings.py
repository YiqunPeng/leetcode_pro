class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """String.

        Running time: O(n1 * n2) where n1 == len(num1) and n2 == len(num2).
        """
        n1, n2 = len(num1), len(num2)
        n12 = n1 + n2
        n = [0] * (n1 + n2)
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                p1 = n12 - i - j - 2
                p2 = p1 + 1
                n[p1] = int(num1[i]) * int(num2[j]) + n[p1]
                c, n[p1] = divmod(n[p1], 10)
                n[p2] += c
        p = len(n) - 1
        while p > 0 and n[p] == 0:
            n.pop()
            p -= 1
        return ''.join([str(i) for i in n[::-1]])
