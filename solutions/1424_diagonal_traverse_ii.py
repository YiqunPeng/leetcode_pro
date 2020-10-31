class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """Array.

        Running time: O(n) where n is total number of elements in nums.
        """
        p = []
        m = len(nums)
        for i in range(m):
            for j in range(len(nums[i])):
                if i + j >= len(p):
                    p.append([nums[i][j]])
                else:
                    p[i+j].append(nums[i][j])
        res = []
        for i in p:
            res.extend(i[::-1])
        return res
