class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """Hash table.

        Running time: O(n) where n is the length of nums.
        """
        c = Counter(nums)
        res = 0
        for k in c:
            if k + 1 in c:
                res = max(res, c[k] + c[k + 1])
        return res
