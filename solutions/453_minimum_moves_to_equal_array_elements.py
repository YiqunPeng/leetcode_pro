class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """Math.

        Running time: O(n) where n == len(nums).
        """
        return sum(nums) - min(nums) * len(nums)
