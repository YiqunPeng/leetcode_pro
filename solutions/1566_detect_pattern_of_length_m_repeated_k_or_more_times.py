class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
    	"""Array.

    	Running time: O(n) where n == len(arr).
    	"""
        if m * k > len(arr):
            return False
        for i in range(0, len(arr) - m * k + 1):
            p = arr[i:i+m]
            if arr[i:i+m*k] == p * k:
                return True
        return False
