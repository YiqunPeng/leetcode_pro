class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """Hash table.

        Running time: O(n) where n is the length of nums.
        """
        d = {0: -1}
        prefix = 0
        for i, num in enumerate(nums):
            prefix += num
            mod = prefix % k
            if mod in d and i - d[mod] > 1:
                return True
            if mod not in d:
                d[mod] = i
        return False
