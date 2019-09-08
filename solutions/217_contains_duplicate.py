class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    	"""Hash set.

    	Running time: O(n) where n is the length of nums.
    	"""
        return len(nums) != len(set(nums))