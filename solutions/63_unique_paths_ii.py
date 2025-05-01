class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """DP.

        Running time: O(MN) where MN is the number of grids in obstacleGrid.
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        n_dp = [0] * n
        dp[0] = 1 - obstacleGrid[0][0]
        n_dp[0] = 1 - obstacleGrid[0][0]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i - 1 >= 0:
                        n_dp[j] += dp[j]
                    if j - 1 >= 0:
                        n_dp[j] += n_dp[j-1]
            dp = n_dp
            n_dp = [0] * n

        return dp[-1]