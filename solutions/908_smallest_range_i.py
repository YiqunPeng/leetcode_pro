class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(A) - min(A) - 2 * K if max(A) - min(A) - 2 * K > 0 else 0
  