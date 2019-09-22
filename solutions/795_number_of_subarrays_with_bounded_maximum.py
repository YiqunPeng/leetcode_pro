class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        """Array.

        Running time: O(n) where n is the length of A.
        """
        lo, li = -1, -1
        ret = 0
        
        for i, a in enumerate(A):
            if a > R:
                lo = i
                continue
            elif L <= a <= R:
                li = i
                ret += i - lo
            else:
                ret += max(0, li - lo)
            
        return ret
