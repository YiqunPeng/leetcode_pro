class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
    	"""Array.

    	Running time: O(n) where n is the length of nums.
    	"""
        for i in range(len(nums)):
            a, b = nums[i], nums[nums[i]-1]
            while a != b and a - 1 != i:
                nums[i], nums[a-1] = b, a
                a, b = nums[i], nums[nums[i]-1]
    
        return [nums[i] for i in range(len(nums)) if nums[i] - 1 != i]