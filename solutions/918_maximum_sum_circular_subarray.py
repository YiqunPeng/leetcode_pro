class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        """Array.

        Running time: O(n) where n == len(A).
        """
        smax, tmax = A[0], A[0]
        smin, tmin = A[0], A[0]
        t = A[0]
        for a in A[1:]:
            tmax = max(tmax + a, a)
            smax = max(tmax, smax)
            tmin = min(tmin + a, a)
            smin = min(tmin, smin)
            t += a
        return max(smax, t - smin) if smax > 0 else smax
