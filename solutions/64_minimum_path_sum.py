class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """DP

        Running Time: O(k) where k is the number of cells in the grid.
        """
        if not grid: 
            return 0
        
        m, n = len(grid), len(grid[0])            
        dp = [sys.maxsize] * n
        
        for i in range(m):    
            for j in range(n):
                if not i and not j:
                    dp[j] = 0
                elif not i:
                    dp[j] = dp[j-1]
                elif j:
                    dp[j] = min(dp[j], dp[j-1])
                
                dp[j] += grid[i][j]
                
        return dp[-1]
  