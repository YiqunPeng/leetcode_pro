class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        """Hash table.

        Running time: O(n * m + k) where k is the length of indices.
        """
        rd, cd = collections.defaultdict(int), collections.defaultdict(int)
        res = 0
        for ri, ci in indices:
            rd[ri] += 1
            cd[ci] += 1
        for i in range(n):
            for j in range(m):
                if (rd[i] + cd[j]) % 2 == 1:
                    res += 1
        return res
