class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """Array.

        Running time: O(n) where n is the length of nums.
        """
        res = 0
        c = 0
        for n in nums:
            if n == 1:
                c += 1
            else:
                res = max(res, c)
                c = 0
        return max(res, c)
