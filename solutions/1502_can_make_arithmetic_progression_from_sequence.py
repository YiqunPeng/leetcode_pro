class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
    	"""Sort.

    	Running time: O(nlogn) where n is the length of arr.
    	"""
        arr.sort()
        for i in range(1, len(arr) - 1):
            if arr[i-1] + arr[i+1] != 2 * arr[i]:
                return False
        return True
