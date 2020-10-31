class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
    	"""Sort.

    	Running time: O(nlogn) where n == len(nums).
    	"""
        n = sorted(nums)
        l = 0
        while l < len(nums) and n[l] == nums[l]:
            l += 1
        r = len(n) - 1
        while r > l and n[r] == nums[r]:
            r -= 1
        return r - l + 1
