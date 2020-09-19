class Solution:
    def findNumbers(self, nums: List[int]) -> int:
    	"""Array.

    	Running time: O(n) where n is the length of nums.
    	"""
        res = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                res += 1
        return res
