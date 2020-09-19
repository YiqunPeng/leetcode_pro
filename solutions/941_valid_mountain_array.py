class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        """Array.

        Running time: O(n) where n is the length of A.
        """
        n = len(A)
        
        if n < 3:
            return False
        
        peak = 0
        for i in range(1, n):
            if A[i] > A[i-1]:
                peak = i
            else:
                break
                
        if peak == 0 or peak == n - 1:
            return False
        
        for i in range(peak+1, n):
            if A[i] >= A[i-1]:
                return False
            
        return True