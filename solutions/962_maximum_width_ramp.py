class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        """Stack.

        Running time: O(n) where n == len(A).
        """
        s = []
        for i in range(len(A)):
            if not s or A[i] < A[s[-1]]:
                s.append(i)
        res = 0
        for i in range(len(A) - 1, -1, -1):
            while s and A[s[-1]] <= A[i]:
                res = max(res, i - s.pop())
        return res
