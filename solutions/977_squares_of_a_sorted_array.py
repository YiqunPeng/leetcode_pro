class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        """Array.

        Running time: O(n) where n is the length of A.
        """
        n = len(A)
        m = abs(A[0])
        p = 0
        for i in range(1, n):
            if abs(A[i]) < abs(m):
                p = i
                m = abs(A[i])
        l, r = p, p + 1
        res = []
        while l >= 0 and r < n:
            if abs(A[l]) <= abs(A[r]):
                res.append(A[l] ** 2)
                l -= 1
            else:
                res.append(A[r] ** 2)
                r += 1
        while l >= 0:
            res.append(A[l] ** 2)
            l -= 1
        while r < n:
            res.append(A[r] ** 2)
            r += 1
        return res
