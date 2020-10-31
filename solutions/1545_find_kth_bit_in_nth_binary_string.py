class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """String.

        Running time: O(n).
        """
        l = 2 ** n - 1
        f = 0
        while k > 1:
            if k == (l + 1) // 2:
                return str(1 ^ f)
            elif k > (l + 1) // 2:
                k = l + 1 - k
                f = 1 - f
            l //= 2
        return str(f)
