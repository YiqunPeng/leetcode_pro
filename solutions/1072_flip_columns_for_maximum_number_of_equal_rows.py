class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        """Hash table.
        """
        d = {}
        for row in matrix:
            v = []
            t = []
            for c in row:
                v.append(c)
                t.append(1 - c)
            d[tuple(v)] = d.get(tuple(v), 0) + 1
            d[tuple(t)] = d.get(tuple(t), 0) + 1
        return max(d.values())
