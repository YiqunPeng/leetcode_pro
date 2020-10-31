class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Running time: O(n) where n == len(nums).
        """
        n = len(nums)
        k %= n
        self._reverse(nums, 0, n - k - 1)
        self._reverse(nums, n - k, n - 1)
        self._reverse(nums, 0, n - 1)
            
    def _reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
