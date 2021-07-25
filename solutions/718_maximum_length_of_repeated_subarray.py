class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        """DP.

        Running time: O(ab) where a == len(A) and b == len(B).
        """
        a, b = len(A), len(B)
        prev = [0] * (b + 1)  
        res = 0
        for i in range(1, a + 1):
            curr = [0] * (b + 1)
            for j in range(1, b + 1):
                if A[i-1] == B[j-1]:
                    curr[j] = prev[j-1] + 1
                    res = max(res, curr[j])
            prev = curr
        return res
