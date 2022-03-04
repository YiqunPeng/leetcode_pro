class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        while l + 1 < len(nums) and nums[l] == nums[l+1]:
            l += 1
        r = len(nums) - 1
        while r > 0 and nums[r] == nums[r-1]:
            r -= 1
        return max(0, r - l - 1)
        