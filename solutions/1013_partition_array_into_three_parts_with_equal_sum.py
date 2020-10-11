class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        """Array.

        Running time: O(n) where n is the length of A.
        """
        r = s = sum(A)
        if s % 3 != 0:
            return False
        p = 0
        c = 0
        t = 2
        sd3 = s // 3
        while t > 0 and p < len(A):
            c += A[p]
            r -= A[p]
            if c == sd3:
                c = 0
                t -= 1
            p += 1
        return p < len(A) and r == sd3
