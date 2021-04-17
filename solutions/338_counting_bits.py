class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        dp = [0] * (num + 1)
        dp[1] = 1
        for i in range(2, num + 1):
            if i % 2 == 1:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i//2]
        return dp
