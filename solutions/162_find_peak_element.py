class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """Binary search.
        """
        nums = [float('-inf')] + nums + [float('-inf')]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid - 1
            elif nums[mid] < nums[mid+1]:
                l = mid + 1
            elif nums[mid] < nums[mid-1]:
                r = mid - 1
