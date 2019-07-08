class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Two Pointers

        Running Time: O(log n) where n is the length of nums.
        """
        l, r = 0, len(nums)
        
        while l < r:
            m = l + (r - l) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m
                
        return -1

    def search_1(self, nums: List[int], target: int) -> int:
        """Two Pointers
        
        Running Time: O(log n) where n is the length of nums.
        """
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + (r - l) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
                
        return -1

    def search_2(self, nums: List[int], target: int) -> int:
        """Recursive

        Running Time: O(log n) where n is the length of nums.
        """
        def recursive(nums, l, r):
            if l >= r:
                return -1
            
            m = l + (r - l) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] < target:
                return recursive(nums, m + 1, r)
            else:
                return recursive(nums, l, m)
            
        return recursive(nums, 0, len(nums))        