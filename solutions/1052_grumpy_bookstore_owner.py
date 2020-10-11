class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        """Sliding window.

        Running time: O(n) where n is the length of customers.
        """
        n = len(customers)
        d = 0
        for i in range(X):
            if grumpy[i] == 1:
                d += customers[i]
        md = d
        for i in range(X, n):
            if grumpy[i-X] == 1:
                d -= customers[i-X]
            if grumpy[i] == 1:
                d += customers[i]
            md = max(d, md)
        res = 0
        for i in range(n):
            if grumpy[i] == 0:
                res += customers[i]
        return res + md
     