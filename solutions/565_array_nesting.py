class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        """DFS.

        Running time: O(n) where n is the length of nums.
        """
        v = set()
        res = 0
        for i in range(len(nums)):
            if i not in v:
                c = 0
                p = i
                while p not in v:
                    v.add(p)
                    p = nums[p]
                    c += 1
                res = max(res, c)
        return res
