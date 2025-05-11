class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """Sliding window.
        """
        i = 0
        k = 0
        for j in range(len(nums)):
            k += 1 - nums[j]
            if k > 1:
                k -= 1 - nums[i]
                i += 1
        return j - i + 1
