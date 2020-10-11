class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        """Array.

        Running time: O(n) where n is the length of A.
        """
        n = len(A)
        for i in range(n - 2, -1, -1):
            if A[i] > A[i + 1]:
                p = self._search(A, i + 1, len(A) - 1, A[i])
                A[i], A[p] = A[p], A[i]
                return A
        return A
    
    def _search(self, A, l, r, v):
        p = r
        while r >= l:
            if A[r] < v:
                if A[p] < v:
                    return p
                p = r
            r -= 1
        return p