class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = mat[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]
        answer = [[0 for j in range(n)] for i in range(m)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                answer[i-1][j-1] = dp[min(m, i+k)][min(n, j+k)] - dp[max(0, i-k-1)][min(n, j+k)] - dp[min(m, i+k)][max(0, j-k-1)] + dp[max(0, i-k-1)][max(0, j-k-1)]
        return answer
