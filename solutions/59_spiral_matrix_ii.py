class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """Array.

        Running time: O(n * n).
        """
        res = [[0] * n for i in range(n)]
        v = 1
        i, j = 0, 0
        while v <= n * n:
            while j < n and res[i][j] == 0:
                res[i][j] = v
                j += 1
                v += 1
            j -= 1
            i += 1
            
            while i < n and res[i][j] == 0:
                res[i][j] = v
                i += 1
                v += 1
            i -= 1
            j -= 1
            
            while j >= 0 and res[i][j] == 0:
                res[i][j] = v
                j -= 1
                v += 1
            j += 1
            i -= 1
            
            while i >= 0 and res[i][j] == 0:
                res[i][j] = v
                i -= 1
                v += 1
            i += 1
            j += 1
            
        return res
