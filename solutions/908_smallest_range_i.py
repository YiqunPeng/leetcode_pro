class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        minv, maxv = A[0], A[0]
        for i in range(1, len(A)):
            minv = min(minv, A[i])
            maxv = max(maxv, A[i])
        return max(0, maxv - K - (minv + K))
