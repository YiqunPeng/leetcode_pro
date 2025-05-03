class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        cells = []
        for i in range(rows):
            for j in range(cols):
                cells.append([(abs(i - rCenter) + abs(j - cCenter)), [i, j]])
        cells.sort(key=lambda x: x[0])
        return [c[1] for c in cells]