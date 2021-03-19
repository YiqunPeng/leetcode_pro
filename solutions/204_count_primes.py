class Solution:
    def countPrimes(self, n: int) -> int:
        """Math.

        Running time: O(n log log n).
        """
        p = [1] * n
        for i in range(2, int(n ** 0.5) + 1):
            if p[i]:
                for j in range(i * i, n, i):
                    p[j] = 0
        return sum(p[2:])
