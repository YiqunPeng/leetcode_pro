class Solution:
    def minFlips(self, target: str) -> int:
        """String.

        Running time: O(n) where n == len(target).
        """
        f = 0
        for i in target:
            if i == '0':
                if f % 2 == 1:
                    f += 1
            else:
                if f % 2 == 0:
                    f += 1
        return f
