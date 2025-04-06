class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """Hash table + prefix sum.

        Running time: O(n) where n == len(nums).
        """
        res = 0
        d = collections.defaultdict(int)
        d[0] = 1
        pre = [0] * (len(nums) + 1)
        for i in range(1, len(pre)):
            pre[i] = pre[i-1] + nums[i-1]
            res += d[pre[i] - k]
            d[pre[i]] += 1          
        return res
