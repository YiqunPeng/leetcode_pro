class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """String.

        Running time: O(n) where n == len(moves).
        """
        r, l, u, d = 0, 0, 0, 0
        for m in moves:
            if m == 'U':
                u += 1
            elif m == 'D':
                d += 1
            elif m == 'R':
                r += 1
            else:
                l += 1
        return u == d and l == r
