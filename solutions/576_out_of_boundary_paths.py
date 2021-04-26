class Solution:
    
    def __init__(self):
        self.mod = 10 ** 9 + 7
        self.memo = {}
    
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        if (i, j, N) in self.memo:
            return self.memo[(i, j, N)]
        paths = 0
        if N == 0:
            return 0
        elif N == 1:
            if i == 0:
                paths += 1
            if i == m - 1:
                paths += 1
            if j == 0:
                paths += 1
            if j == n - 1:
                paths += 1
        else:
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if ni < 0 or ni == m:
                    paths += 1
                    continue
                if nj < 0 or nj == n:
                    paths += 1
                    continue
                paths += self.findPaths(m, n, N - 1, ni, nj)
        self.memo[(i, j, N)] = paths
        return paths % self.mod
