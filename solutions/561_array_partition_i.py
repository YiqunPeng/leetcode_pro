class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
    	"""Sort.

    	Running time: O(nlogn) where n is the length of nums.
    	"""
        nums.sort()
        return sum(nums[::2])
