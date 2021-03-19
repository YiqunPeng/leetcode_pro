class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    	"""Bit manipulation.

    	Running time: O(n) where n == len(nums).
    	"""
        res = 0
        for n in nums:
            res ^= n
        return res
