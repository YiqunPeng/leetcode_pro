class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    	"""Array.

    	Running time: O(n) where n == len(nums).
    	"""
        if not nums:
            return 0
        maxp, minp = nums[0], nums[0]
        res = nums[0]
        for num in nums[1:]:
            x = max(maxp * num, minp * num, num)
            y = min(minp * num, maxp * num, num)
            maxp, minp = x, y
            res = max(maxp, res)
        return res
