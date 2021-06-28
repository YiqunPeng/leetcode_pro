class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        first = self._binary_search(nums, target - 1)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        last = self._binary_search(nums, target) - 1
        return [first, last]
    
    def _binary_search(self, nums, t):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if t >= nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        return hi
