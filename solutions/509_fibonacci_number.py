class Solution:
    def fib(self, N: int) -> int:
        """Array. 

        Running time: O(N).
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        m, n = 0, 1
        for i in range(2, N + 1):
            f = m + n
            m = n 
            n = f
        return n
