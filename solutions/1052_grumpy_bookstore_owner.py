class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        """Sliding window.

        Running time: O(n) where n is the length of customers.
        """
        n = len(customers)        
        if n <= X:
            return sum(customers)
     
        s = 0
        m = e = sum(c for c in customers[:X] if c == 1)        
        
        for i in range(1, n - X + 1):
            if grumpy[i-1] == 1:
                e -= customers[i-1]
            if grumpy[i+X-1] == 1:
                e += customers[i+X-1]
            if e > m:
                s = i
                m = e

        return sum(customers[i] for i in range(n) if s <= i < s + X or grumpy[i] == 0)
     