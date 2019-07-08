class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """ 
        l, r = 1, len(A) - 1
        
        while l < r:
            m = l + (r - l) // 2
            
            if A[m-1] < A[m] > A[m+1]:
                return m
            elif A[m] < A[m+1]:
                l = m + 1
            else:
                r = m
        