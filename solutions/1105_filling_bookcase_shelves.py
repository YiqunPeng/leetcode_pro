class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)
        for i in range(n):
            dp[i+1] = dp[i] + books[i][1]
            w, h = 0, 0
            for j in range(i, -1, -1):
                if books[j][0] + w > shelf_width:
                    break
                w += books[j][0]
                h = max(h, books[j][1])
                dp[i+1] = min(dp[i+1], dp[j] + h)
        return dp[-1]
