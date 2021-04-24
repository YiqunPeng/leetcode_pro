class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1.0
        return 1 / n + (n - 2) / n * self.nthPersonGetsNthSeat(n - 1)
