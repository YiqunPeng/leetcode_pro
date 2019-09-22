class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        """DP.

        Running time: O(8 ^ K)
        """
        directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
                      (1, -2), (2, -1), (2, 1), (1, 2)]
        
        pos = {(r, c): 1.0}
        
        while K:
            npos = collections.defaultdict(float)
            for i, j in pos.keys():
                for di in directions:
                    ni, nj = i + di[0], j + di[1]
                    if 0 <= ni < N and 0 <= nj < N:
                        npos[(ni, nj)] += pos[(i, j)] / 8
            pos = npos
            K -= 1
        
        return sum(pos.values())
