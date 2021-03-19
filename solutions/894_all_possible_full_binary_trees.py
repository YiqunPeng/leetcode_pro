class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        """DP.
        """
        if N % 2 == 0:
            return []
        dp = [[] for i in range(N + 1)]
        dp[1] = [TreeNode(0)]
        for n in range(3, N + 1, 2):
            for i in range(1, n - 1, 2):
                j = n - 1 - i
                for lt in dp[i]:
                    for rt in dp[j]:
                        root = TreeNode(0, lt, rt)
                        dp[n].append(root)
        return dp[-1]
