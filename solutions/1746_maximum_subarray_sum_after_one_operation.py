class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        n = len(nums)
        a, b = nums[0], nums[0] * nums[0]
        res = b
        for i in range(1, n):
            b = max(max(0, a) + nums[i] * nums[i], b + nums[i])
            a = max(0, a) + nums[i]
            res = max(res, b)
        return res
