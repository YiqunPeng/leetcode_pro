class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """Array.

        Running time: O(numRows^2)
        """
        res = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(i + 1):
                if j != 0 and j != i:
                    row[j] = res[i-1][j-1] + res[i-1][j]
            res.append(row)
        return res
