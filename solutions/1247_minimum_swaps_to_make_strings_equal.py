class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        """String.

        Running time: O(n) where n == len(s1).
        """
        x1, y1 = 0, 0
        x2 = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    x1 += 1
                else:
                    y1 += 1
                    x2 += 1
        if (x1 + x2) % 2 == 1:
            return -1
        else:
            return x1 // 2 + y1 // 2 + 2 * (x1 % 2)
