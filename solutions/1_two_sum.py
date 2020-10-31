class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Hash table.

        Running time: O(n) where n == len(nums).
        """
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]] = [i]
        for k, v in d.items():
            if target - k in d:
                if target - k == k and len(v) >= 2:
                    return [v[0], v[1]]
                elif target - k != k:
                    return [v[0], d[target-k][0]]
