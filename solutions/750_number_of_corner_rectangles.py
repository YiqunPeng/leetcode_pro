class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        rows = []
        for row in grid:
            curr = set()
            for i in range(n):
                if row[i] == 1:
                    curr.add(i)
            for prev in rows:
                v = len(curr & prev)
                res += (v - 1) * v // 2
            rows.append(curr)
        return res
