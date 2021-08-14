class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """Sliding window.
        """
        k = 1
        i = 0
        for j in range(len(nums)):
            k -= 1 - nums[j]
            if k < 0:
                k += 1 - nums[i]
                i += 1
        return j - i + 1
