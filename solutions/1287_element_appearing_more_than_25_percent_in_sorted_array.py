class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
    	"""Array.

    	Running time: O(n) where n is the length of arr.
    	"""
        for i in range(len(arr)):
            if arr[i] == arr[i + len(arr) // 4]:
                return arr[i]
