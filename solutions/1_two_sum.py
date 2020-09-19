class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	"""Hash map.

    	Running time: O(n) where n is the length of nums.
    	"""
        d = {}
        for i, num in enumerate(nums):
            if target == num * 2 and num in d:
                return i, d[num]
            d[num] = i
            
        for i, num in enumerate(nums):
            if target - num in d and d[target-num] != i:
                return i, d[target-num]