class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        lamp = set()
        row, col, diag, adiag = {}, {}, {}, {}
        for r, c in lamps:
            if (r, c) in lamp:
                continue    
            lamp.add((r, c))
            row[r] = row.get(r, 0) + 1
            col[c] = col.get(c, 0) + 1
            diag[r+c] = diag.get(r+c, 0) + 1
            adiag[r-c+n-1] = adiag.get(r-c+n-1, 0) + 1 

        res = []
        for r, c in queries:
            if row.get(r, 0) > 0 or col.get(c, 0) > 0 or diag.get(r+c, 0) > 0 or adiag.get(r-c+n-1, 0) > 0:
                res.append(1)
            else:
                res.append(0)
            for i in range(-1, 2):
                for j in range(-1, 2):
                    nr, nc = r + i, c + j
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) in lamp:
                        lamp.remove((nr, nc))
                        row[nr] = row.get(nr, 0) - 1
                        col[nc] = col.get(nc, 0) - 1
                        diag[nr+nc] = diag.get(nr+nc, 0) - 1
                        adiag[nr-nc+n-1] = adiag.get(nr-nc+n-1, 0) - 1 
        return res