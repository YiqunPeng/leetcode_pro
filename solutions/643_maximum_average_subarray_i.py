class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    	"""Array.

    	Running time: O(n) where n == len(nums).
    	"""
        s = sum(nums[:k])
        m = s
        for i in range(k, len(nums)):
            s = s - nums[i - k] + nums[i]
            m = max(m, s)
        return m / float(k)
