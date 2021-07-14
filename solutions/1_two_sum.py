class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Hash table.

        Running time: O(n) where n == len(nums).
        """
        d = {nums[0]: 0}
        for i in range(1, len(nums)):
            if target - nums[i] in d:
                return [i, d[target - nums[i]]]
            d[nums[i]] = i
