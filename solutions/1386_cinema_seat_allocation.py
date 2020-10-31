class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        """Hash table.

        Running time: O(r) where r == len(reservedSeats).
        """
        rd = {}
        for i, j in reservedSeats:
            if 2 <= j <= 9:
                if i not in rd:
                    rd[i] = [0, 0, 0, 0]
                rd[i][(j - 2)//2] = 1
        res = 2 * n
        for k, v in rd.items():
            if sum(v) == 1:
                res -= 1
            elif sum(v) == 2:
                if v == [1, 0, 0, 1] or v == [1, 1, 0, 0] or v == [0, 0, 1, 1]:
                    res -= 1
                else:
                    res -= 2
            else:
                res -= 2
        return res
