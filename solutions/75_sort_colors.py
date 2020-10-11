class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Running time: O(n) where n == len(nums).
        """
        n = len(nums)
        l, r, p = 0, n - 1, 0
        while p <= r:
            if nums[p] == 0:
                nums[p], nums[l] = nums[l], 0
                l, p = l + 1, p + 1
            elif nums[p] == 2:
                nums[p], nums[r] = nums[r], 2
                r -= 1
            else:
                p += 1
