class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
    	"""Frequency table.

    	Running time: O(n) where n is the length of nums.
    	"""
        c = collections.Counter(nums)
        res = 0
        for k, v in c.items():
            res += (v - 1) * v // 2
        return res
