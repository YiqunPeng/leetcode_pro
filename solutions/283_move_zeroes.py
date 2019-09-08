class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Array.
        
        Running time: O(n) where n is the length of nums.
        """
        p = 0
        
        for num in nums:
            if num != 0:
                nums[p] = num
                p += 1
        
        for i in range(p, len(nums)):
            nums[i] = 0 
        