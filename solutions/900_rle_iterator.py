class RLEIterator:

    def __init__(self, A: List[int]):
        self.p = 0
        self.A = A

    def next(self, n: int) -> int:
        """Array.
        
        Running time: O(k) where k is the length of self.A.
        """
        while n > 0 and self.p < len(self.A):
            if self.A[self.p] >= n:
                self.A[self.p] -= n
                return self.A[self.p+1]
            else:
                n -= self.A[self.p]
                self.A[self.p] = 0
                self.p += 2
        return -1  
