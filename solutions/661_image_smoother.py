class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        if not M:
            return None
        
        m, n = len(M), len(M[0])
        ret = [[0] * n for i in range(m)]
        
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 0), (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        
        for i in range(m):
            for j in range(n):
                s, cnt = 0, 0 
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < m and 0 <= nj < n:
                        s += M[ni][nj]
                        cnt += 1
                ret[i][j] = s // cnt
        
        return ret
