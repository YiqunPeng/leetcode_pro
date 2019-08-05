class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
    	"""Array.

		Running time: O(n) where n is the length of nums.
    	"""
        for num in nums:
            if nums[abs(num)-1] < 0:
                return abs(num)
            nums[abs(num)-1] *= -1
