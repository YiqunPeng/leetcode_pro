class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """Hash table.

        Running time: O(n) where n == len(nums).
        """
        res = 0
        d = collections.defaultdict(int)
        d[0] = 1
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            res += d[s - k]
            d[s] += 1
        return res
