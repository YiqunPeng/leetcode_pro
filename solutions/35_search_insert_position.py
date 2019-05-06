class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """Binary Search

        Running Time: O(n log n) where n is the length of nums.
        """
        l, r = 0, len(nums) - 1
        
        if nums[l] > target:
            return 0
        if nums[r] < target:
            return r + 1
        
        while l <= r:
            m = l + (r - l) // 2
            
            if target == nums[m]:
                return m 
            elif nums[m] < target < nums[m+1]:
                return m + 1
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
