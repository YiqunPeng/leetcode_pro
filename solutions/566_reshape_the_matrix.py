class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        """Array.

        Running time: O(r*c).
        """
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        p = 0
        res = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(nums[p//n][p%n])
                p += 1
            res.append(row)
        return res
