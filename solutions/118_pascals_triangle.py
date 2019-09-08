class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """Math.

        Running time: O(numRows^2)
        """
        ret = []
        
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                    continue
                row.append(ret[i-1][j-1] + ret[i-1][j])
            ret.append(row)
        
        return ret