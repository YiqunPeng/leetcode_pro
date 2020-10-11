class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        """Presum array.

        Running time: O(n) where n is the length of A.
        """
        n = len(A)
        psum = [0] * (n + 1)
        for i in range(n):
            psum[i+1] = psum[i] + A[i]
        res = psum[L+M]
        lmax, mmax = psum[L] - psum[0], psum[M] - psum[0]
        for i in range(L+M, n):
            lmax = max(lmax, psum[i-M+1] - psum[i-M-L+1])
            mmax = max(mmax, psum[i-L+1] - psum[i-M-L+1])
            res = max(res, lmax + psum[i+1] - psum[i-M+1], mmax + psum[i+1] - psum[i-L+1])
        return res
