class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        s = nums[0]
        for num in nums[1:]:
            s = max(num, num + s)
            res = max(res, s)
        return res
