class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        """Array.

        Running time: O(n) where n == len(A).
        """
        n = len(A)
        l = A[:]
        for i in range(1, n - 1):
            l[i] = max(l[i-1], A[i])
        r = A[:]
        for i in range(n - 2, 0, -1):
            r[i] = min(r[i+1], A[i])
        for i in range(n - 1):
            if l[i] <= r[i+1]:
                return i + 1
