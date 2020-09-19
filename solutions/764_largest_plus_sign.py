class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        """DP.

        Running time: O(N*N).
        """
        mines = set(tuple(mine) for mine in mines)    
        counts = [[0] * N for i in range(N)]
        
        res = 0
        
        for i in range(N):
            c = 0
            for j in range(N):
                c = 0 if (i, j) in mines else c + 1
                counts[i][j] = c
            
            c = 0
            for j in range(N - 1, -1, -1):
                c = 0 if (i, j) in mines else c + 1
                counts[i][j] = min(counts[i][j], c)
                    
        for j in range(N):
            c = 0
            for i in range(N):
                c = 0 if (i, j) in mines else c + 1
                counts[i][j] = min(counts[i][j], c)
            
            c = 0
            for i in range(N - 1, -1, -1):
                c = 0 if (i, j) in mines else c + 1
                counts[i][j] = min(counts[i][j], c)
                    
                res = max(res, counts[i][j])

        return res
              