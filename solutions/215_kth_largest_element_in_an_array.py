class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Quick select.

        Running time: O(n) where n == len(nums).
        """
        left, right = 0, len(nums) - 1
        idx = -1
        while idx != k - 1:
            idx = self._partition(nums, left, right)
            if idx < k - 1:
                left = idx + 1
            else:
                right = idx - 1
        return nums[idx]
    
    def _partition(self, nums, left, right):
        pivot = nums[left]
        l, r = left + 1, right
        while l <= r:
            if nums[l] < pivot < nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            elif nums[l] >= pivot:
                l += 1
            elif nums[r] <= pivot:
                r -= 1
        nums[left], nums[r] = nums[r], nums[left]
        return r
