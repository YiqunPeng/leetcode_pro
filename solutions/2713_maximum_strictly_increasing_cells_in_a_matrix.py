class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        """DP.
        """
        m, n = len(mat), len(mat[0])
        vals = defaultdict(list)
        for i in range(m):
            for j in range(n):
                vals[mat[i][j]].append((i, j))
        
        dp = [[0] * n for i in range(m)]
        rows = [0] * m
        cols = [0] * n

        for k in sorted(vals):
            for i, j in vals[k]:
                dp[i][j] = max(dp[i][j], rows[i] + 1, cols[j] + 1)
            
            for i, j in vals[k]:
                rows[i] = max(rows[i], dp[i][j])
                cols[j] = max(cols[j], dp[i][j])
        
        return max(max(rows), max(cols))