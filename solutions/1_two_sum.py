class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Hash table.

        Running time: O(n) where n == len(nums).
        """
        d = {}
        for i, v in enumerate(nums):
            if target - v in d:
                return [d[target - v], i]
            d[v] = i
