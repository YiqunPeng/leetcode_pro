class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
    	"""Array.

    	Running time: O(n) where n is the length of arr.
    	"""
        for i in range(1, len(arr) - 1):
            if arr[i-1] % 2 == arr[i] % 2 == arr[i+1] % 2 == 1:
                return True
        return False
