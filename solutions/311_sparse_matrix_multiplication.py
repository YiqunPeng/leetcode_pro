class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """Hash table.
        """
        ma, na = len(A), len(A[0])
        mb, nb = len(B), len(B[0])
        res = [[0] * nb for i in range(ma)]
        da = {}
        db = {}
        for i in range(ma):
            for j in range(na):
                if A[i][j]:
                    da[(i, j)] = A[i][j]
        for i in range(mb):
            for j in range(nb):
                if B[i][j]:
                    db[(i, j)] = B[i][j]
        for ka, va in da.items():
            for kb, vb in db.items():
                if ka[1] == kb[0]:
                    res[ka[0]][kb[1]] += va * vb
        return res
