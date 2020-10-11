class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        """Array.

        Running time: O(n^2).
        """
        d = {}
        for x, y in pairs:
            d[x] = y
            d[y] = x
        rank = [[0] * n for i in range(n)]
        for i in range(n):
            r = n - 1
            for f in preferences[i]:
                rank[i][f] = r
                r -= 1
        res = 0
        for x, y in pairs:
            xh, yh = True, True
            for u in range(n):
                v = d[u]
                if xh and rank[x][u] > rank[x][y] and rank[u][x] > rank[u][v]:
                    res += 1
                    xh = False
                if yh and rank[y][u] > rank[y][x] and rank[u][y] > rank[u][v]:
                    res += 1
                    yh = False
        return res
