class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        """Array. Math.

        Running time: O(n) where n == len(A).
        """
        n = len(A)
        p = 0
        while p < n - 1:
            if A[p] == p:
                p += 1
            elif A[p] == p + 1 and A[p + 1] == p:
                p += 2
            else:
                return False
        return True
