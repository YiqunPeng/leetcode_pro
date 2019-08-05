class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int: 
        """Array.

        Running time: O(nlogn) where n is the length of A.
        """ 
        if not A: 
            return 0

        A.sort()
        m = 0
        cur = A[0]
        
        for a in A[1:]:
            if a <= cur:
                m += (cur + 1 - a)
                cur += 1
            cur = max(cur, a)
    
        return m
