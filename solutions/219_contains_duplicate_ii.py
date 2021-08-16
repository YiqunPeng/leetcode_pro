class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    	"""Hash table.

    	Running time: O(n) where n is the length of nums.
    	"""
        d = {}
        for i in range(len(nums)):
            if nums[i] in d and i - d[nums[i]] <= k:
                return True
            d[nums[i]] = i
        return False
