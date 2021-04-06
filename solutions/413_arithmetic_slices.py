class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 1
        while r + 1 < len(nums):
            if nums[r+1] - nums[r] != nums[l+1] - nums[l]:
                res += (r - l) * (r - l - 1) // 2
                l = r
            r += 1
        return res + (r - l) * (r - l - 1) // 2
