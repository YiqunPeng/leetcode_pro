class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
    	"""String.

    	Running time: O(n) where n == len(nums).
    	"""
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])
        else:
            return str(nums[0]) + '/(' + '/'.join([str(i) for i in nums[1:]]) + ')'
