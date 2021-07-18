class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Array.

        Running time: O(n) where n == len(nums).
        """
        if not nums:
            return None
        n = len(nums)
        p = n - 1
        while p > 0 and nums[p] <= nums[p-1]:
            p -= 1
        if p == 0:
            self._reverse(nums, 0, n - 1)
            return
        pos = p - 1
        q = n - 1
        while q > pos and nums[q] <= nums[pos]:
            q -= 1
        nums[pos], nums[q] = nums[q], nums[pos]
        return self._reverse(nums, pos + 1, n - 1)
        
    def _reverse(self, nums, s, e):
        while s < e and s < len(nums):
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1
