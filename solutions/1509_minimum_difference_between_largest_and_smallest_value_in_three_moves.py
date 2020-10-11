class Solution:
    def minDifference(self, nums: List[int]) -> int:
    	"""Sort.

    	Running time: O(nlogn) where n is the length of nums.
    	"""
        if len(nums) <= 3:
            return 0
        nums.sort()   
        return min(nums[-4] - nums[0], nums[-3] - nums[1], nums[-2] - nums[2], nums[-1] - nums[3])
