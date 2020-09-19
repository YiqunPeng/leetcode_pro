class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """DP.

        Running time: O(k) where k is the number of grids in obstacleGrid.
        """
        if not obstacleGrid:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0] * n for i in range(m)]
        
        dp[0][0] = 1 - obstacleGrid[0][0]
        
        p = 1
        while p < n and obstacleGrid[0][p] == 0:
            dp[0][p] = dp[0][p-1]
            p += 1
            
        p = 1
        while p < m and obstacleGrid[p][0] == 0:
            dp[p][0] = dp[p-1][0]
            p += 1
            
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    continue
                
                if i - 1 >= 0:
                    dp[i][j] += dp[i-1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j-1]
        
        return dp[-1][-1]