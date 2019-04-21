class Solution:
    def myPow(self, x: float, n: int) -> float:
        """Binary Search

        Running Time: O(log n)
        """
        if n == 0:
            return 1.0
        if n == 1:
            return x
        
        if n < 0:
            n = -n
            x = 1.0 / x
        
        t = self.myPow(x, n // 2)
        return t * t * self.myPow(x, n % 2)
        