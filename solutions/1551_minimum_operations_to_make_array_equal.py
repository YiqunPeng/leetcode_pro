class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 1:
            n_2 = n // 2
            return n_2 ** 2 + n_2
        else:
            n_2 = n // 2
            return n_2 ** 2
