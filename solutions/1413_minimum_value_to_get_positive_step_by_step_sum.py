class Solution:
    def minStartValue(self, nums: List[int]) -> int:
    	"""Array.

    	Running time: O(n) where n is the length of nums.
    	"""
        s = nums[0]
        m = s
        for i in range(1, len(nums)):
            s += nums[i]
            m = min(m, s)
        return max(1, 1 - m)
