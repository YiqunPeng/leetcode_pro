class Solution:
    def myPow(self, x: float, n: int) -> float:
        """Binary Search, Recursive

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
 
    def myPow_2(self, x: float, n: int) -> float:
        """Binary Search, Iterative

        Running Time: O(log n)
        """
        if n < 0:
            n = -n
            x = 1 / x
            
        ret = 1
            
        while n:
            if n % 2:
               ret *= x
            x *= x
            n //= 2
        
        return ret 
      