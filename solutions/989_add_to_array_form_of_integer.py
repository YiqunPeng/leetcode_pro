class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
    	"""Array.

    	Running time: O(n) where n == len(A).
    	"""
        n = len(A)
        for i in range(n - 1, -1, -1):
            K, A[i] = divmod(A[i] + K, 10)
        return [int(i) for i in str(K)] + A if K else A
