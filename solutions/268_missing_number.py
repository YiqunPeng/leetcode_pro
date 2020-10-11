class Solution:
    def missingNumber(self, nums: List[int]) -> int:
    	"""Math.

    	Running time: O(n) where n is the length of nums.
    	"""
        return sum(range(len(nums)+1)) - sum(nums)
