class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        """Binary search.

        Running time: O(nlogn) where n is the length of nums.
        """
        f = self._first_apperance(nums, target)
        l = self._last_apperance(nums, target)
        return True if l - f + 1 > len(nums) // 2 else False
    
    def _first_apperance(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l
    
    def _last_apperance(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return r
